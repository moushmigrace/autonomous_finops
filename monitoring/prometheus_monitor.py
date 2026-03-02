import requests
import random

from shared.logger import get_logger
from shared.constants import PROMETHEUS_URL


class PrometheusMonitor:

    def __init__(self, namespace, deployment, use_mock=False, prometheus_url=PROMETHEUS_URL):

        self.logger = get_logger("PrometheusMonitor")

        self.namespace = namespace
        self.deployment = deployment
        self.use_mock = use_mock
        self.url = prometheus_url.rstrip("/")


    def get_metrics(self):

        if self.use_mock:
            return self._mock_metrics()

        cpu = self._safe_query(self._cpu_query())
        memory = self._safe_query(self._memory_query())
        traffic = self._safe_query(self._traffic_query())

        metrics = {
            "cpu": cpu,
            "memory": memory,
            "traffic": traffic
        }

        self.logger.info(f"Prometheus metrics: {metrics}")

        return metrics


    def _cpu_query(self):

        # CPU cores used
        return f'''
        sum(rate(container_cpu_usage_seconds_total{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}[2m]))
        '''


    def _memory_query(self):

        return f'''
        sum(container_memory_usage_bytes{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}) / 1024 / 1024
        '''


    def _traffic_query(self):

        return f'''
        sum(rate(http_requests_total{{
            namespace="{self.namespace}",
            pod=~"{self.deployment}.*"
        }}[1m]))
        '''


    def _safe_query(self, query):

        try:
            return self._execute(query)
        except Exception as e:
            self.logger.warning(f"Prometheus query failed: {e}")
            return 0


    def _execute(self, query):

        response = requests.get(
            f"{self.url}/api/v1/query",
            params={"query": query},
            timeout=5
        )

        data = response.json()

        if not data["data"]["result"]:
            return 0

        cores = float(data["data"]["result"][0]["value"][1])

        # convert cores → percentage
        cpu_percent = cores * 100

        return round(cpu_percent, 2)


    def _mock_metrics(self):

        return {
            "cpu": random.uniform(10, 90),
            "memory": random.uniform(100, 500),
            "traffic": random.uniform(0, 1000)
        }