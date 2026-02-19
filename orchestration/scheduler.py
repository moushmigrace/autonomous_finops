import time
from shared.logger import get_logger
from shared.constants import SCHEDULER_INTERVAL


class Scheduler:

    def __init__(self, supervisor):

        self.logger = get_logger("Scheduler")

        self.supervisor = supervisor


    def start(self):

        self.logger.info("Scheduler started")

        while True:

            self.supervisor.run_cycle()

            time.sleep(SCHEDULER_INTERVAL)