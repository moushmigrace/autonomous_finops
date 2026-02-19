#!/bin/bash

set -e

CLUSTER_NAME="finops-cluster"
REGION="us-east-1"

echo "Updating kubeconfig..."

aws eks update-kubeconfig \
  --region $REGION \
  --name $CLUSTER_NAME

echo "Cluster connected successfully."

kubectl get nodes