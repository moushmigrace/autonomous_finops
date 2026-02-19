import requests
import random
from shared.logger import get_logger
from shared.constants import PROMETHEUS_URL


class PrometheusMonitor:

    def __init__(
        self,
        namespace="default",
        deployment="backend-app",
        use_mock=False,
        prometheus_url=PROMETHEUS_URL,
        timeout=5
    ):

        self.logger = get_logger("PrometheusMonitor")

        self.namespace = namespace
        self.deployment = deployment
        self.use_mock = use_mock
        self.url = prometheus_url.rstrip("/")
        self.timeout = timeout


    def get_metrics(self):

        if self.use_mock:
            return self._mock_metrics()

        try:

            cpu = self._query_cpu()
            memory = self._query_memory()
            traffic = self._query_traffic()

            return {
                "cpu": cpu,
                "memory": memory,
                "traffic": traffic
            }

        except Exception:

                self.logger.info("Using MOCK Prometheus metrics")

                return self._mock_metrics()


    def _query_cpu(self):

        query = f"""
        sum(rate(container_cpu_usage_seconds_total{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}[1m])) * 100
        """

        return self._execute(query)


    def _query_memory(self):

        query = f"""
        sum(container_memory_usage_bytes{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}) / 1024 / 1024
        """

        return self._execute(query)


    def _query_traffic(self):

        query = f"""
        sum(rate(http_requests_total{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}[1m]))
        """

        return self._execute(query)


    def _execute(self, query):

        response = requests.get(
            f"{self.url}/api/v1/query",
            params={"query": query},
            timeout=self.timeout
        )

        data = response.json()

        if not data["data"]["result"]:
            return 0.0

        value = float(data["data"]["result"][0]["value"][1])

        return round(value, 2)


    def _mock_metrics(self):

        return {
            "cpu": round(random.uniform(1, 100), 2),
            "memory": round(random.uniform(50, 500), 2),
            "traffic": round(random.uniform(0, 1000), 2)
        }