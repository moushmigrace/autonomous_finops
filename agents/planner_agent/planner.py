from shared.constants import IDLE_CPU_THRESHOLD
from shared.logger import get_logger

logger = get_logger("PlannerAgent")


class PlannerAgent:

    def plan(self, metrics):

        actions = []

        for m in metrics:

            if m["cpu"] < IDLE_CPU_THRESHOLD and m["replicas"] > 0:

                actions.append({
                    "action": "scale_down",
                    "deployment": m["deployment"],
                    "replicas": 0,
                    "namespace": m["namespace"]
                })

                logger.info(f"Planning scale down: {m['deployment']}")

        return actions