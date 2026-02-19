from monitoring.prometheus_monitor import PrometheusMonitor
from monitoring.kubernetes_monitor import KubernetesMonitor
from monitoring.parser import MetricsParser


class MetricsCollector:

    def __init__(
        self,
        namespace="default",
        deployment="backend-app",
        use_mock=False
    ):

        self.prom = PrometheusMonitor(
            namespace,
            deployment,
            use_mock
        )

        self.k8s = KubernetesMonitor(
            namespace,
            deployment,
            use_mock
        )

        self.parser = MetricsParser()


    def collect(self):

        prom_data = self.prom.get_metrics()

        k8s_data = self.k8s.get_deployment_info()

        parsed = self.parser.normalize(
            prom_data,
            k8s_data
        )

        return parsed