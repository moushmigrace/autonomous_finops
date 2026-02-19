from execution.k8s_scaler import K8sScaler

class ExecutorAgent:

    def __init__(self):

        self.scaler = K8sScaler()

    def execute(self, actions):

        for action in actions:

            if action["action"] == "scale_down":

                self.scaler.scale(
                    action["namespace"],
                    action["deployment"],
                    action["replicas"]
                )