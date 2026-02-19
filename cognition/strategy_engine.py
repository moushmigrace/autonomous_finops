from shared.logger import get_logger


class StrategyEngine:

    def __init__(self):

        self.logger = get_logger("StrategyEngine")


    def optimize(self, decision, metrics):

        cpu = metrics["cpu"]

        if cpu < 10:

            decision["strategy"] = "cost_saving"

        elif cpu > 70:

            decision["strategy"] = "performance"

        else:

            decision["strategy"] = "balanced"

        self.logger.info(f"Strategy selected: {decision}")

        return decision