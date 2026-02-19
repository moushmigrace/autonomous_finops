from shared.config_loader import load_config
from shared.logger import get_logger


class ReasoningEngine:

    def __init__(self):

        self.logger = get_logger("ReasoningEngine")

        self.thresholds = load_config("configs/thresholds.yaml")

        self.rules = load_config("configs/scaling_rules.yaml")


    def decide(self, metrics, prediction):

        cpu = metrics["cpu"]
        memory = metrics["memory"]
        replicas = metrics["replicas"]

        scale_down_threshold = self.thresholds["cpu_scale_down"]
        scale_up_threshold = self.thresholds["cpu_scale_up"]

        predicted = prediction["expected_replicas"]

        decision = {
            "action": "none",
            "replicas": replicas
        }

        if cpu < scale_down_threshold:

            decision["action"] = "scale"
            decision["replicas"] = 0

        elif cpu > scale_up_threshold:

            decision["action"] = "scale"
            decision["replicas"] = predicted

        else:

            decision["action"] = "maintain"
            decision["replicas"] = replicas

        self.logger.info(f"Decision: {decision}")

        return decision