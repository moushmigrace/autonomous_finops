from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

from shared.logger import get_logger
from shared.constants import (
    KUBERNETES_IN_CLUSTER,
    MIN_REPLICAS,
    MAX_REPLICAS
)


class K8sScaler:

    def __init__(self):

        self.logger = get_logger("K8sScaler")

        try:
            if KUBERNETES_IN_CLUSTER:
                config.load_incluster_config()
            else:
                config.load_kube_config()

            self.api = client.AppsV1Api()

            self.logger.info("K8sScaler initialized successfully")

        except ConfigException as e:

            self.logger.error(f"Kubernetes config failed: {e}")
            raise


    def scale(self, namespace, deployment, replicas):

        # Safety limits
        replicas = max(MIN_REPLICAS, replicas)
        replicas = min(MAX_REPLICAS, replicas)

        body = {
            "spec": {
                "replicas": replicas
            }
        }

        self.api.patch_namespaced_deployment_scale(
            name=deployment,
            namespace=namespace,
            body=body
        )

        self.logger.info(f"Scaled deployment {deployment} to {replicas}")