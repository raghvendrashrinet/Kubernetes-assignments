
```
  http://localhost:8081/
         ↓
  [Ingress Controller] (port 8081 mapped from host)
         ↓
  [Ingress Rules] (path: / → hashresponse-svc:2345)
         ↓
  [Service] (port 2345 → targetPort 3000)
         ↓
  [Pod] (container listening on port 3000)
         ↓
  [Application]
```
Ingress log
```
Projects\1.7 Ingress> kubectl.exe get ingress
NAME                   CLASS     HOSTS   ADDRESS                            PORTS   AGE
dwk-material-ingress   traefik   *       172.19.0.2,172.19.0.3,172.19.0.5   80      69m
Projects\1.7 Ingress> kubectl.exe describe ingress dwk
Name:             dwk-material-ingress
Labels:           <none>
Namespace:        default
Address:          172.19.0.2,172.19.0.3,172.19.0.5
Ingress Class:    traefik
Default backend:  <default>
Rules:
  Host        Path  Backends
  ----        ----  --------
  *
              /   hashgenerator-svc:2345 (10.42.0.14:3000)
Annotations:  <none>
Events:       <none>

```
