from shared.logger import get_logger


class LearningAgent:

    def __init__(self):

        self.logger = get_logger("LearningAgent")


    def learn(self, metrics, actions, result):

        self.logger.info("Learning from execution")

        # Future: train ML model here

        return True