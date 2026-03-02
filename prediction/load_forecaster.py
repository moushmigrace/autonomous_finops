import math

class LoadForecaster:

    def __init__(self, forecast_steps=3):
        self.forecast_steps = forecast_steps

    def forecast(self, cpu_history):

        if len(cpu_history) < 3:
            return cpu_history[-1] if cpu_history else 0

        # Simple linear trend
        start = cpu_history[0]
        end = cpu_history[-1]

        slope = (end - start) / len(cpu_history)

        # Forecast future CPU
        forecast_cpu = end + slope * self.forecast_steps

        return max(0, forecast_cpu)