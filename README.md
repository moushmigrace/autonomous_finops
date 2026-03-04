Autonomous FinOps Agent for Kubernetes :

An Agentic AI-driven FinOps system that autonomously monitors Kubernetes workloads, predicts resource demand, and performs intelligent cost-aware scaling of applications.

This project extends traditional Kubernetes autoscaling by introducing forecast-based scaling, idle environment optimization, and autonomous decision-making.

📌 Project Overview

Cloud infrastructure often wastes resources due to idle environments and reactive autoscaling strategies. Traditional tools like Horizontal Pod Autoscaler (HPA) only react to current metrics.

This project introduces an Autonomous FinOps Agent that:

Continuously monitors Kubernetes workloads

Predicts near-future resource demand

Optimizes replica counts

Detects idle environments

Reduces cloud infrastructure cost

The system runs inside the Kubernetes cluster as a containerized agent.

🧠 Agentic AI Architecture

The system follows an agent-based control loop:

Sense → Think → Decide → Act

Architecture workflow:

Prometheus Metrics
        ↓
Monitoring Agent
        ↓
Short-Term Memory
        ↓
Predictor Agent
        ↓
Planner Agent
        ↓
Executor Agent
        ↓
Kubernetes API
        ↓
Deployment Scaling

Each module performs a specific role in the autonomous decision pipeline.

🔍 Key Features
📊 Real-Time Monitoring

Collects Kubernetes CPU, memory, and pod metrics

Uses Prometheus and Kubernetes metrics server

📈 Proportional Scaling

Instead of incremental scaling (+1 pod), the system uses proportional scaling:

Desired Replicas = Current Replicas × (Current CPU / Target CPU)
🔮 Predictive Scaling

Short-term workload forecasting

Uses CPU trend analysis stored in short-term memory

💤 Idle Environment Detection

Detects idle development or staging deployments

Automatically scales them to zero replicas

🔄 Cooldown Protection

Prevents scaling oscillation by applying cooldown windows.

💰 FinOps Optimization

Focuses on reducing cloud infrastructure cost while maintaining performance.

🏗 Project Architecture
Developer Environment
    ↓
WSL Ubuntu
    ↓
Docker + KIND Cluster
    ↓
GitHub Repository
    ↓
GitHub Actions CI/CD
    ↓
Terraform Infrastructure
    ↓
AWS EKS Cluster
    ↓
Prometheus Monitoring
    ↓
FinOps Agent
    ↓
Kubernetes API
    ↓
Application Scaling
⚙️ Technology Stack
Component	Technology
Containerization	Docker
Kubernetes	EKS / KIND
Programming	Python
Monitoring	Prometheus
Infrastructure	Terraform
CI/CD	GitHub Actions
Local Dev	WSL Ubuntu
Backend Service	Node.js
📂 Project Structure
autonomous-finops-agent
│
├── agents
│   ├── monitor_agent
│   ├── planner_agent
│   ├── executor_agent
│   ├── predictor_agent
│   └── learning_agent
│
├── monitoring
│   ├── metrics_collector.py
│   ├── prometheus_monitor.py
│   └── kubernetes_monitor.py
│
├── memory
│   ├── short_term_memory.py
│   ├── long_term_memory.py
│   └── vector_store.py
│
├── execution
│   ├── k8s_scaler.py
│   └── deployment_manager.py
│
├── cognition
│   ├── policy_engine.py
│   ├── reasoning_engine.py
│   └── strategy_engine.py
│
├── deployment
│   ├── docker
│   └── kubernetes
│
├── infrastructure
│   └── terraform
│
├── monitoring
├── configs
├── main.py
└── requirements.txt
💻 Local Development Environment

The project was initially tested using:

WSL Ubuntu

Docker

KIND (Kubernetes in Docker)

This allowed simulation of Kubernetes scaling behavior locally before deploying to the cloud.

Example command to create KIND cluster:

kind create cluster --name finops-cluster
☁️ Cloud Deployment

Infrastructure was deployed using Terraform on AWS EKS.

Terraform provisions:

Kubernetes cluster

Worker nodes

Networking configuration

IAM roles

Deployment pipeline automatically creates infrastructure and deploys the application.

🔄 CI/CD Pipeline

The project includes a GitHub Actions CI/CD pipeline.

Pipeline stages:

Checkout repository

Build Docker images

Push images to registry

Configure AWS credentials

Deploy infrastructure using Terraform

Deploy application and FinOps agent

This enables fully automated infrastructure and application deployment.

📊 Demonstration of Proportional Scaling

Scaling behavior was demonstrated using:

WSL Ubuntu environment

KIND Kubernetes cluster

CPU load was generated using:

curl http://localhost:4000/cpu-stress

Observed behavior:

CPU spike
   ↓
FinOps Agent detects load
   ↓
Planner calculates new replicas
   ↓
Executor scales deployment
   ↓
Pods increase
⚠️ Real Deployment Challenge (AWS Free Tier)

The system was deployed on AWS EKS free-tier infrastructure.

Cluster configuration:

Instance type: t3.micro
Nodes: 2

Due to AWS ENI limits, each node supports only ~4 pods.

Since system pods consume some slots:

aws-node
kube-proxy
coredns
metrics-server

Application pods were limited to ~3–4 replicas.

This caused additional pods to remain Pending when scaling beyond cluster capacity.

🧠 Engineering Insight

This demonstrated an important real-world principle:

Autoscaling algorithms can request more replicas, but the actual scaling depends on cluster infrastructure capacity.

In production environments, this would be solved using Cluster Autoscaler, which automatically provisions additional nodes.

📈 Example Scaling Flow
User Requests Increase
        ↓
CPU Utilization Increases
        ↓
Prometheus Metrics Collected
        ↓
FinOps Agent Analysis
        ↓
Planner Calculates Replicas
        ↓
Executor Applies Scaling
        ↓
Kubernetes Creates Pods
🎯 Future Improvements

Reinforcement learning-based scaling

Long-term workload forecasting

Budget-aware scaling policies

Multi-cluster optimization

Integration with Kubernetes Cluster Autoscaler

📚 Key Learnings

This project provided practical experience in:

Kubernetes autoscaling mechanisms

Infrastructure as Code with Terraform

CI/CD pipelines for cloud-native systems

Prometheus-based monitoring

FinOps cost optimization strategies

Agent-based autonomous systems

📌 Author

Moushmi Grace

Cloud | Kubernetes | DevOps | Platform Engineering Enthusiast

⭐ If you like this project

Feel free to star the repository and share feedback!
