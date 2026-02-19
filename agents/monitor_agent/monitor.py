from monitoring.kubernetes_monitor import KubernetesMonitor
from monitoring.prometheus_monitor import PrometheusMonitor
from shared.logger import get_logger


class MonitorAgent:

    def __init__(self):

        self.logger = get_logger("MonitorAgent")

        self.kube = KubernetesMonitor()

        self.prom = PrometheusMonitor()


    def collect(self):

        deployments = self.kube.get_deployments()

        metrics = []

        for dep in deployments:

            prom_metrics = self.prom.get_metrics()

            metrics.append({

                "deployment": dep["name"],

                "cpu": prom_metrics["cpu"],

                "memory": prom_metrics["memory"],

                "traffic": prom_metrics["traffic"],

                "replicas": dep["replicas"],

                "namespace": dep["namespace"]
            })

        self.logger.info(f"Collected metrics: {metrics}")

        return metrics