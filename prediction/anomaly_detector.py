class AnomalyDetector:

    def detect(self, metrics):

        return metrics["cpu"] > 95 or metrics["memory"] > 95