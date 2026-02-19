import numpy as np

class PredictorAgent:

    def predict(self, cpu_history):

        if len(cpu_history) < 2:
            return cpu_history[-1]

        trend = np.polyfit(range(len(cpu_history)), cpu_history, 1)

        future = trend[0] * len(cpu_history) + trend[1]

        return max(0, future)