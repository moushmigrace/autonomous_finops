from shared.logger import get_logger


class CostAgent:

    def __init__(self):

        self.logger = get_logger("CostAgent")


    def calculate(self, metrics, actions):

        savings = 0

        for action in actions:

            if action["action"] == "scale_down":

                savings += 10  # mock saving

        self.logger.info(f"Estimated savings: ${savings}")

        return savings