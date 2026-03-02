from monitoring.kubernetes_monitor import KubernetesMonitor
from monitoring.prometheus_monitor import PrometheusMonitor

from shared.logger import get_logger
from shared.constants import (
    K8S_NAMESPACE,
    K8S_DEPLOYMENT_NAME,
    PROMETHEUS_USE_MOCK
)


class MonitorAgent:

    def __init__(self):

        self.logger = get_logger("MonitorAgent")

        # Kubernetes monitor
        self.kube = KubernetesMonitor()

        # FIX: Pass required arguments to PrometheusMonitor
        self.prom = PrometheusMonitor(
            namespace=K8S_NAMESPACE,
            deployment=K8S_DEPLOYMENT_NAME,
            use_mock=PROMETHEUS_USE_MOCK
        )


    def collect(self):

        deployments = self.kube.get_deployments()

        metrics = []

        for dep in deployments:

            prom_metrics = self.prom.get_metrics()

            metrics.append({

                "deployment": dep["name"],

                "namespace": dep["namespace"],

                "cpu": prom_metrics["cpu"],

                "memory": prom_metrics["memory"],

                "traffic": prom_metrics["traffic"],

                "replicas": dep["replicas"]
            })

        self.logger.info(f"Collected metrics: {metrics}")

        return metrics