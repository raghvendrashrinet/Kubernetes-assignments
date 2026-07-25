# Todo App (Project 2.8 - Step 11)

A full-stack Todo application running on Kubernetes, featuring a Python Flask backend, a Python Flask frontend, and a PostgreSQL database.

## Project Structure
```
├── Frontend/
│   ├── frontend.py           # Talks to todo-backend via HTTP
│   └── Dockerfile
└── manifests/
    ├── 01-Configmap.yaml     # ConfigMap (POSTGRES_HOST, DB, USER, PORT, etc.)
    ├── postgres-db.yaml      # Secret + Service + StatefulSet for Postgres
    ├── backend-deployment.yaml
    ├── backend-svc.yaml
    ├── frontend-deployment.yaml
    ├── frontend-svc.yaml
    └── ingress.yaml
```
#### Application Access & Architecture Flow
Frontend-> Backend -> DB Flow 
```
Frontend -> Backend -> DB Flow

+-------------------+
|   User Request    |
|   (HTTP / API)    |
+-------------------+
          |
          v
+------------------------------------+
|   App Pod Logic                    |
|------------------------------------|
| 1. Read Env Variables:             |
|    - POSTGRES_HOST (postgres-svc)  |
|    - POSTGRES_DB (todo_db)         |
|    - POSTGRES_USER (todo_user)     |
|    - POSTGRES_PASSWORD (Secret)    |
|    - POSTGRES_PORT (5432)          |
| 2. init_db() on startup            |
|    Creates table if not exists     |
| 3. Connect directly via psycopg2   |
+------------------------------------+
          |
          v
+-------------------+
|   DB Service      |
|   ClusterIP:5432  |
+-------------------+
          |
          v
+-----------------------------+
|   DB Pod (PostgreSQL)       |
|-----------------------------|
| 1. Parse SQL string         |
| 2. Execute query            |
| 3. Return result set        |
+-----------------------------+
          |
          v
+-------------------+
|   App Pod Logic   |
|-------------------|
| 4. Process rows   |
| 5. Format JSON    |
| 6. Send response  |
+-------------------+
          |
          v
+-------------------+
|   User Response   |
+-------------------+
```

#### Code Logic & Database Access
1. Direct PostgreSQL Connection (psycopg2)
The backend connects directly to PostgreSQL using parameters supplied via environment variables (POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_PORT).

2. Automatic Schema Initialization (init_db)
Upon backend startup, init_db() runs automatically to ensure the todos table is created before accepting incoming HTTP requests:
```sql
CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL
);
```
3. API Endpoints
```
GET /todos: Fetches all existing todo items from the database.

POST /todos: Inserts a new todo item into the database.
```
Deployment Steps
Apply Configuration & Secrets:

```Bash
kubectl apply -f manifests/01-Configmap.yaml
```
Deploy PostgreSQL Database:

```Bash
kubectl apply -f manifests/postgres-db.yaml
```
Deploy Backend, Frontend & Ingress:

```Bash
kubectl apply -f manifests/backend-deployment.yaml
kubectl apply -f manifests/backend-svc.yaml
kubectl apply -f manifests/frontend-deployment.yaml
kubectl apply -f manifests/frontend-svc.yaml
kubectl apply -f manifests/ingress.yaml
```

