# Exercise 1.7 - Hash Generator Web Application with Ingress

This project builds upon the logic of Exercise 1.3 by introducing a containerized web server that allows external traffic to fetch the dynamically generated hash and timestamp. Routing is handled by a **Traefik Ingress Controller**.

---

## 🚀 Application Logic & Architecture

The application has transitioned from a pure background logging script to a web service:
* **Background Worker:** Continuously generates a random hash string upon startup and logs it to the console alongside a timestamp every 5 seconds.
* **Web Server:** Listens on a designated port (e.g., `3000`) and serves the latest hash and timestamp via an HTTP endpoint.
* **Ingress Routing (Traefik):** Traefik acts as the entry point to the cluster, securely routing external HTTP requests to the application's underlying Kubernetes Service.

---

## 🛠 Development & Testing

### 1. Deploy the manifest

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
###  test the url on web browser
```
 http://localhost:8081/
```
