from shared.config_loader import load_config
from shared.logger import get_logger


class PolicyEngine:

    def __init__(self, config_path="configs/policies.yaml"):

        self.logger = get_logger("PolicyEngine")

        self.policies = load_config(config_path)


    def apply(self, decision):

        min_replicas = self.policies["min_replicas"]
        max_replicas = self.policies["max_replicas"]
        allow_scale_to_zero = self.policies["allow_scale_to_zero"]

        replicas = decision["replicas"]

        if replicas == 0 and not allow_scale_to_zero:
            replicas = min_replicas

        replicas = max(min_replicas, replicas)
        replicas = min(max_replicas, replicas)

        decision["replicas"] = replicas

        self.logger.info(f"Policy applied: {decision}")

        return decision