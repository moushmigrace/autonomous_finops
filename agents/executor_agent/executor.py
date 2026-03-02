from execution.k8s_scaler import K8sScaler

class ExecutorAgent:

    def __init__(self):

        self.scaler = K8sScaler()

    def execute(self, actions):

        for action in actions:

            namespace = action["namespace"]
            deployment = action["deployment"]
            desired = action["desired_replicas"]

            self.scaler.scale(
              namespace,
              deployment,
              desired
        )