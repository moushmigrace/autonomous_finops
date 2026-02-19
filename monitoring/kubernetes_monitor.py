from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException
from shared.logger import get_logger
from shared.constants import (
    KUBERNETES_IN_CLUSTER,
    K8S_NAMESPACE,
    K8S_DEPLOYMENT_NAME,
    PROMETHEUS_USE_MOCK
)


class KubernetesMonitor:

    def __init__(self):

        self.logger = get_logger("KubernetesMonitor")

        self.namespace = K8S_NAMESPACE
        self.deployment = K8S_DEPLOYMENT_NAME
        self.use_mock = PROMETHEUS_USE_MOCK

        if self.use_mock:

            self.logger.info("Using MOCK Kubernetes monitor")

            self.apps = None

            return

        try:

            if KUBERNETES_IN_CLUSTER:

                config.load_incluster_config()

                self.logger.info("Loaded in-cluster Kubernetes config")

            else:

                config.load_kube_config()

                self.logger.info("Loaded local kubeconfig")

            self.apps = client.AppsV1Api()

        except ConfigException:

            self.logger.warning("Kubernetes config not found. Using MOCK mode")

            self.use_mock = True
            self.apps = None


    def get_deployments(self):

        if self.use_mock:

            return [
                {
                    "name": self.deployment,
                    "replicas": 2,
                    "namespace": self.namespace
                }
            ]

        dep = self.apps.read_namespaced_deployment(

            name=self.deployment,

            namespace=self.namespace
        )

        return [
            {
                "name": dep.metadata.name,
                "replicas": dep.spec.replicas,
                "namespace": dep.metadata.namespace
            }
        ]