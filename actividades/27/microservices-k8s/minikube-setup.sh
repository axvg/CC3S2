#!/bin/bash
# Script para inicializar Minikube y desplegar servicios

echo "Iniciando Minikube..."
minikube start --driver=docker

echo "Construyendo imágenes Docker..."
# Configura el entorno Docker para usar el daemon de Minikube
eval "$(minikube -p minikube docker-env --shell bash)"

minikube kubectl -- get pods -A

docker build -t user-service:latest service-user
docker build -t order-service:latest service-order

echo "Desplegando en Kubernetes..."
# Aplica las configuraciones de despliegue
minikube kubectl -- apply --filename k8s/user-deployment.yaml
minikube kubectl -- apply --filename k8s/order-deployment.yaml

echo "Servicios desplegados:"
# Muestra los servicios en el clúster
minikube kubectl get svc

minikube dashboard