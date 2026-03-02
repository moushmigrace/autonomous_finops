from shared.logger import get_logger


class Supervisor:

    def __init__(self, monitor, predictor, planner, executor, learner, cost):

        self.logger = get_logger("Supervisor")

        self.monitor = monitor
        self.predictor = predictor
        self.planner = planner
        self.executor = executor
        self.learner = learner
        self.cost = cost


    def run_cycle(self):

        self.logger.info("Starting FinOps cycle")

        metrics = self.monitor.collect()

        self.logger.info(f"Collected metrics: {metrics}")

        predictions = []

        for metric in metrics:
            cpu = metric["cpu"]
            prediction = self.predictor.predict(cpu)
            predictions.append({
                "deployment": metric["deployment"],
                "predicted_cpu": prediction
            })

        self.logger.info(f"Predictions: {predictions}")

        actions = self.planner.plan(metrics)

        result = self.executor.execute(actions)

        self.learner.learn(metrics, actions, result)

        savings = self.cost.calculate(metrics, actions)

        self.logger.info(f"Cost savings: {savings}")

        return result