from kubernetes import client, config


class DeploymentManager:

    def __init__(self, namespace="default", use_mock=False):

        self.namespace = namespace

        self.use_mock = use_mock

        if not use_mock:

            try:
                config.load_incluster_config()
            except:
                config.load_kube_config()

            self.api = client.AppsV1Api()


    def get_deployment(self, name):

        if self.use_mock:

            return {"name": name, "replicas": 2}

        return self.api.read_namespaced_deployment(

            name=name,

            namespace=self.namespace
        )