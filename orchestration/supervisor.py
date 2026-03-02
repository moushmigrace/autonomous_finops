from shared.logger import get_logger
from shared.constants import *
import time


class Supervisor:

    def __init__(self, monitor, predictor, planner, executor, learner, cost):

        self.logger = get_logger("Supervisor")

        self.monitor = monitor
        self.predictor = predictor
        self.planner = planner
        self.executor = executor
        self.learner = learner
        self.cost = cost

        # Cooldown protection
        self.last_scale_time = 0

        # Idle tracking
        self.idle_tracker = {}

    def run_cycle(self):

        self.logger.info("Starting FinOps cycle")

        metrics = self.monitor.collect()
        self.logger.info(f"Collected metrics: {metrics}")

        now = time.time()

        # =============================
        # 1️⃣ Idle tracking logic
        # =============================
        for m in metrics:

            key = m["deployment"]
            cpu = m["cpu"]
            traffic = m["traffic"]

            if cpu < IDLE_CPU_THRESHOLD and traffic == 0:

                if key not in self.idle_tracker:
                    self.idle_tracker[key] = now

                idle_for = now - self.idle_tracker[key]

            else:
                self.idle_tracker.pop(key, None)
                idle_for = 0

            m["idle_for"] = idle_for

        # =============================
        # 2️⃣ Planning
        # =============================
        actions = self.planner.plan(metrics)

        # =============================
        # 3️⃣ Cooldown enforcement
        # =============================
        if actions:
            if now - self.last_scale_time < COOLDOWN_PERIOD:
                self.logger.info("Cooldown active — skipping scaling")
                return None

            self.last_scale_time = now

        # =============================
        # 4️⃣ Execute
        # =============================
        result = self.executor.execute(actions)

        self.learner.learn(metrics, actions, result)

        savings = self.cost.calculate(metrics, actions)

        self.logger.info(f"Cost savings: {savings}")

        return result