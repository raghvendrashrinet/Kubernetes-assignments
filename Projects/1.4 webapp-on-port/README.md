# Web App on Specific Port

This project demonstrates how to build a containerized web application, push it to Docker Hub, and manage its runtime ports using both Kubernetes (Deployments) and Docker.

### 1. Build the Docker Image
```bash
docker build -t raghvendrashrinet/projects:1.4 .
```
### 2. Run Using Docker and Check Locally
```
docker run raghvendrashrinet/projects:1.4

Server started in port 3000
```

### 3. Push to Docker Hub
```
docker push raghvendrashrinet/projects:1.4
```
### 4. Deploy to Kubernetes
```
kubectl apply -f manifest/
```
### 5. Verify the Deployment

```
kubectl get pods
kubectl logs webapp-69cf9bbbdf-2d4mt
Server started in port 3000
```
6. Access via Port-Forwarding
```
kubectl port-forward deployment/webapp 3000:3000

Forwarding from 127.0.0.1:3000 -> 3000

## Browse : http://localhost:3000
```

