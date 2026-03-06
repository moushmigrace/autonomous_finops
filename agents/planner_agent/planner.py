from shared.constants import *
from shared.logger import get_logger
from agents.cost_agent.cost import CostAgent
from prediction.load_forecaster import LoadForecaster
from memory.short_term_memory import ShortTermMemory
import math

logger = get_logger("PlannerAgent")


class PlannerAgent:

    def __init__(self):
        self.cost_agent = CostAgent()
        self.memory = ShortTermMemory(window=10)
        self.forecaster = LoadForecaster()

    def plan(self, metrics):

        actions = []

        for m in metrics:

            deployment = m["deployment"]
            namespace = m["namespace"]

            cpu = m["cpu"]
            traffic = m["traffic"]
            replicas = m["replicas"]
            idle_for = m.get("idle_for", 0)

            # Store CPU history
            self.memory.store(deployment, cpu)
            cpu_history = self.memory.get(deployment)

            forecast_cpu = self.forecaster.forecast(cpu_history)

            desired = replicas

            # Idle-to-zero
            if idle_for > IDLE_DURATION_THRESHOLD:
                desired = 0

            else:

                if replicas > 0:
                    desired = math.ceil(
                        replicas * cpu / TARGET_CPU
                    )

                # Proactive forecast scaling
                if forecast_cpu > TARGET_CPU:
                    desired += 1

                # Traffic-based scaling
                if traffic > 100:
                    desired += 1

            # Cost optimization
            desired = self.cost_agent.optimize(cpu, desired,idle_for)

            # Safety
            desired = max(0, desired)
            desired = min(MAX_REPLICAS, desired)

            if desired != replicas:

                logger.info(
                    f"Scaling decision: {deployment} "
                    f"{replicas} → {desired} "
                    f"(cpu={cpu}, forecast_cpu={forecast_cpu}, idle_for={idle_for})"
                )

                actions.append({
                    "namespace": namespace,
                    "deployment": deployment,
                    "current_replicas": replicas,
                    "desired_replicas": desired,
                    "reason": {
                        "cpu": cpu,
                        "forecast_cpu": forecast_cpu,
                        "idle_for": idle_for
                    }
                })

        return actions