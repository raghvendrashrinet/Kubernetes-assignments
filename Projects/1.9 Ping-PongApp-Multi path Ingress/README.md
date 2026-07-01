
## Annotation for URL rewriting Nginx vs Traefik Middleware Setup


#### The Problem
When you host multiple applications under different sub-paths on the same domain, the backend applications often expect to serve traffic directly from the root path (`/`) and do not naturally recognize the external sub-path prefix.nize the external sub-path prefix 

In our current scenario, both microservices are actively listening on /:

Hash Generator App: Listens on /

Ping Pong App: Listens on / 
```                
                            /
                            |
                            |
                            |
              -----------------------------
              |                            |
              |                            |
              |                            |
         Hash generator app          Ping pong app 
         listen on (/)                listen on (/)
```

#### The Goal
To configure our Ingress resource so that traffic splits seamlessly based on the sub-path:
 - Hash Generator App $\rightarrow$ `http://localhost:8081/`
 - Ping Pong App $\rightarrow$ `http://localhost:8081/pingpong`
##### To achieve this without changing our application source code, we use middleware/annotations to strip the prefix out before the request hits the backend pod. This way, the apps perfectly resolve the requests as they only ever see a standard / request.
---
## Nginx vs. Traefik
## Nginx :The annotation 
`nginx.ingress.kubernetes.io/rewrite-target: /` is used in Kubernetes Nginx Ingress resources to rewrite the request URI before forwarding it to the backend service.

## Traefik: since our Controller is Traefik, we require to approach as below
Traefik handles this decoupling via a custom CRD called a Middleware.
#### Use Traefik Middleware
**1. Create the Middleware Save this as `strip-prefix.yaml`:**
 ```
  apiVersion: traefik.containo.us/v1alpha1
  kind: Middleware
  metadata:
    name: strip-pingpong
    namespace: default
  spec:
    stripPrefix:
      prefixes:
        - /pingpong
 ```
 - Apply `kubectl apply -f strip-prefix.yaml   `
**2. Update ingress annotation with the Traefik middleware annotation:**
 ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
    name: ingress1
    annotations:
    # REMOVE the nginx annotation below
    # nginx.ingress.kubernetes.io/rewrite-target: / 
    
    # ADD this Traefik annotation (format: <namespace>-<name>@kubernetescrd)
    traefik.ingress.kubernetes.io/router.middlewares: default-strip-pingpong@kubernetescrd
  spec:
   # ... rest of your config
 ```
```
USER BROWSER
    │
    ├── 1. http://localhost:8081/
    └── 2. http://localhost:8081/pingpong
        ▼
┌─────────────────┐      ┌───────────────────────────────────────────────────────────────────┐
│ LOCAL MACHINE   │ ───► │ K3D CLUSTER (Traefik Ingress Controller)                          │
│ Port Forward    │      │ Listens: Port 80 (Mapped from 8081)                               │
│ 8081 → 80       │      │                                                                   │
└─────────────────┘      │  ┌─────────────────────────────────────────────────────────────┐  │
                         │  │ ROUTING LOGIC                                               │  │
                         │  │                                                             │  │
                         │  │  Path: "/" ─────────────────────────────────────────┐       │  │
                         │  │         │                                           |       │  │  │
                         │  │         ▼                                           │       │  │  │
                         │  │  Path: "/pingpong"                                  │       │  │
                         │  │         │                                           │       │  │
                         │  │         ▼                                           │       │  │
                         │  │  [MIDDLEWARE: strip-pingpong] ◄─── PREFIX STRIPPED  │       │  │
                         │  │  Action: Strip "/pingpong" prefix                   │       │  │
                         │  │         │                                           │       │  │
                         │  └─────────┼───────────────────────────────────────────┼───────│  │
                         └────────────┼───────────────────────────────────────────┼───────┘ ─┘
                                      │ (Request becomes "/")                     │
                                      ▼                                           ▼
                        ┌─────────────────────┐                     ┌─────────────────────┐
                        │ SERVICE: pong-app   │                     │ SERVICE:            │
                        │ Port: 8000          │                     │ hashgenerator-svc   │
                        │ IP: 10.42.0.27      │                     │ Port: 2345          │
                        │                     │                     │ IP: 10.42.0.26      │
                        │ ✅ Receives: "/"    │                     │                     │
                        │ ✅ Returns: 200 OK  │                     │ ✅ Receives: "/"    │
                        └─────────────────────┘                     │ ✅ Returns: 200 OK  │
                                                                    └─────────────────────┘
```
  
