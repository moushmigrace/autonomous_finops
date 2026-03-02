class PredictorAgent:

    def __init__(self):

        self.history = []

        self.window = 10


    def predict(self, cpu):

        cpu = float(cpu)

        self.history.append(cpu)

        if len(self.history) > self.window:
            self.history.pop(0)

        if len(self.history) < 3:
            return cpu

        # moving average prediction
        avg = sum(self.history) / len(self.history)

        # detect upward trend
        trend = self.history[-1] - self.history[0]

        predicted = avg + (trend * 0.5)

        return max(0, predicted)