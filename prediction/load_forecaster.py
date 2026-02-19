class LoadForecaster:

    def forecast(self, metrics):

        cpu = metrics["cpu"]

        if cpu > 70:

            return {"expected_replicas": 5}

        if cpu < 10:

            return {"expected_replicas": 0}

        return {"expected_replicas": 2}