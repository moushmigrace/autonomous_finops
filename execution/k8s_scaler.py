from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException
from shared.logger import get_logger
from shared.constants import (
    KUBERNETES_IN_CLUSTER,
    K8S_NAMESPACE,
    PROMETHEUS_USE_MOCK
)


class K8sScaler:

    def __init__(self):

        self.logger = get_logger("K8sScaler")

        self.namespace = K8S_NAMESPACE

        self.use_mock = PROMETHEUS_USE_MOCK

        if self.use_mock:

            self.logger.info("Using MOCK scaler")

            self.api = None

            return

        try:

            if KUBERNETES_IN_CLUSTER:

                config.load_incluster_config()

            else:

                config.load_kube_config()

            self.api = client.AppsV1Api()

        except ConfigException:

            self.logger.warning("Scaler falling back to MOCK mode")

            self.use_mock = True
            self.api = None


    def scale(self, namespace, deployment, replicas):

        if self.use_mock:

            self.logger.info(f"[MOCK] Scaling {deployment} to {replicas}")

            return

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

        self.logger.info(f"Scaled {deployment} to {replicas}")