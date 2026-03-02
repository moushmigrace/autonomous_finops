from shared.constants import *
from shared.logger import get_logger
from agents.cost_agent.cost import CostAgent
from agents.predictor_agent.predictor import PredictorAgent

logger = get_logger("PlannerAgent")


class PlannerAgent:

    def __init__(self):

        self.cost_agent = CostAgent()
        self.predictor = PredictorAgent()

    def plan(self, metrics):

        actions = []

        for m in metrics:

            deployment = m["deployment"]
            namespace = m["namespace"]

            cpu = m["cpu"]
            traffic = m["traffic"]
            replicas = m["replicas"]

            predicted_cpu = self.predictor.predict(cpu)

            desired = replicas

            # CPU scaling
            if cpu > SCALE_UP_THRESHOLD:
                desired += 1

            elif cpu < SCALE_DOWN_THRESHOLD:
                desired -= 1

            # Traffic scaling
            if traffic > 100:
                desired += 1

            # Predictive scaling
            if predicted_cpu > SCALE_UP_THRESHOLD:
                desired += 1

            # Cost optimization
            desired = self.cost_agent.optimize(cpu, desired)

            # Safety limits
            desired = max(MIN_REPLICAS, desired)
            desired = min(MAX_REPLICAS, desired)

            if desired != replicas:

                logger.info(
                    f"Scaling decision: {deployment} "
                    f"{replicas} → {desired} "
                    f"(cpu={cpu}, traffic={traffic}, predicted={predicted_cpu})"
                )

                actions.append({
                   "namespace": namespace,
                   "deployment": deployment,
                   "current_replicas": replicas,
                   "desired_replicas": desired,
                   "reason": {
                      "cpu": cpu,
                     "traffic": traffic,
                      "predicted_cpu": predicted_cpu
                  }
})

        return actions