class MetricsParser:

    def normalize(self, prom_data, k8s_data):

        return {

            "cpu": float(prom_data.get("cpu", 0)),

            "memory": float(prom_data.get("memory", 0)),

            "traffic": float(prom_data.get("traffic", 0)),

            "replicas": int(k8s_data.get("replicas", 0)),

            "available_replicas": int(
                k8s_data.get("available_replicas", 0)
            )
        }