# Web App on Specific Port

This project demonstrates how to build a containerized web application, push it to Docker Hub, and manage its runtime ports using both Kubernetes (Pods and Deployments) and Docker.

---

## 1. Build and Push the Image

First, build your Docker image and push it to Docker Hub so Kubernetes can pull it:

```bash
# Build the Docker image
docker build -t raghvendrashrinet/projects:1.2 .
```
```
# Push the image to Docker Hub
docker push raghvendrashrinet/projects:1.2
```
## 2. Running the Application in Kubernetes  
Run as a Pod with a Custom Port
```bash
kubectl run my-app --image=raghvendrashrinet/projects:1.2 --env="PORT=3005" --port=3005 todo-app
```
### Understanding the Flags:  
- --env="PORT=3005": Required. This sets the environment variable inside the container, instructing your Node.js/Python application to actively listen on port 3005.
- --port=3005: Optional (Metadata). This populates the containerPort field in the Pod's configuration (spec.containers[0].ports) for documentation purposes.If you omit --port=3005, the application will still run and listen on port 3005 internally because Kubernetes does not block container ports by default.

### 3. Accessing the Application (Port Forwarding)

```
# Format: kubectl port-forward pod/<pod-name> <host-port>:<container-port>
kubectl port-forward pod/todo-app 3000:3000
```
