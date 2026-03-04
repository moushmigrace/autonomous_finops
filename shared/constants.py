# shared/constants.py

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==============================
# CPU thresholds (%)
# ==============================

IDLE_CPU_THRESHOLD = 10
SCALE_UP_THRESHOLD = 30
SCALE_DOWN_THRESHOLD = 10

# ==============================
# Replica limits (read from .env)
# ==============================

IDLE_DURATION_THRESHOLD = int(os.getenv("IDLE_DURATION_THRESHOLD", "300"))  # 5 min
COOLDOWN_PERIOD = int(os.getenv("COOLDOWN_PERIOD", "120"))  # 2 min
TARGET_CPU = int(os.getenv("TARGET_CPU", "30"))

MIN_REPLICAS = int(os.getenv("MIN_REPLICAS", "1"))
MAX_REPLICAS = int(os.getenv("MAX_REPLICAS", "10"))
DEFAULT_REPLICAS = int(os.getenv("DEFAULT_REPLICAS", "2"))

# ==============================
# Scheduler / Monitor intervals
# ==============================

SCHEDULER_INTERVAL = int(os.getenv("MONITOR_INTERVAL", "30"))
MONITOR_INTERVAL = int(os.getenv("MONITOR_INTERVAL", "30"))

# ==============================
# Cost settings
# ==============================

FORECAST_WINDOW = 5
FORECAST_THRESHOLD = 65
PREDICTIVE_ENABLED = True

COST_PER_REPLICA = float(os.getenv("COST_PER_REPLICA", "0.01"))

# ==============================
# Prometheus configuration
# ==============================

PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090"
)

PROMETHEUS_TIMEOUT = int(os.getenv("PROMETHEUS_TIMEOUT", "5"))

PROMETHEUS_USE_MOCK = os.getenv(
    "PROMETHEUS_USE_MOCK",
    "true"
).lower() == "true"

# ==============================
# Kubernetes configuration
# ==============================

K8S_NAMESPACE = "finops"
K8S_DEPLOYMENT_NAME = "backend-app"

KUBERNETES_IN_CLUSTER = True

# ==============================
# AWS configuration
# ==============================

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

EKS_CLUSTER_NAME = os.getenv(
    "EKS_CLUSTER_NAME",
    "finops-cluster"
)

# ==============================
# Registry configuration
# ==============================

CONTAINER_REGISTRY = os.getenv(
    "CONTAINER_REGISTRY",
    "ghcr.io"
)

REGISTRY_IMAGE_PREFIX = os.getenv(
    "REGISTRY_IMAGE_PREFIX",
    ""
)