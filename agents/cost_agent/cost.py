from shared.logger import get_logger
from shared.constants import COST_PER_REPLICA, MIN_REPLICAS, MAX_REPLICAS


class CostAgent:

    def __init__(self):

        self.logger = get_logger("CostAgent")


    def optimize(self, cpu, replicas):

        """
        Optimize replica count based on CPU and cost efficiency
        """

        original = replicas

        # If CPU very low → reduce replicas
        if cpu < 10 and replicas > MIN_REPLICAS:

            replicas -= 1

        # If CPU very high → increase replicas
        elif cpu > 80 and replicas < MAX_REPLICAS:

            replicas += 1

        if replicas != original:

            self.logger.info(
                f"Cost optimization adjusted replicas: {original} → {replicas}"
            )

        return replicas


    def calculate(self, metrics, actions):

        """
        Calculate cost savings from scaling actions
        """

        total_cost_before = 0
        total_cost_after = 0

        for m in metrics:

            replicas_before = m["replicas"]

            replicas_after = replicas_before

            for action in actions:

                if action["deployment"] == m["deployment"]:

                    replicas_after = action["desired_replicas"]
                    break

            total_cost_before += replicas_before * COST_PER_REPLICA

            total_cost_after += replicas_after * COST_PER_REPLICA

        savings = total_cost_before - total_cost_after

        self.logger.info(
            f"Cost before: {total_cost_before:.4f}, "
            f"after: {total_cost_after:.4f}, "
            f"savings: {savings:.4f}"
        )

        return savings