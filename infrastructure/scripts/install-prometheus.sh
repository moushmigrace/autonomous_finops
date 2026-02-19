#!/bin/bash

set -e

echo "Installing Prometheus..."

helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts

helm repo update

kubectl create namespace monitoring || true

helm install prometheus \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring

echo "Prometheus installed."

kubectl get pods -n monitoring