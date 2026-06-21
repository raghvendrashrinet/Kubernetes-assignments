## How it works
1. Python code : `app.py`
2. install Flask, and run it(checlk app locally):
   ```bash
    pip install flask
    python app.py
   ```

3. Go to `http://localhost:3000` in your browser to see it run.

---
### Publish image , prepare kubernetes manifest and run

```
## Building image and push to docker hub
docker build -t raghvendrashrinet/projects:1.5 .
docker push raghvendrashrinet/projects:1.5

## Create app 
kubectl.exe apply -f .\manifests\
## Forward host port to check the app 
kubectl port-forward pod/web-server-5bdf487bdc-f4b2b 3000:3000


##Browse
http://localhost:3000/
http://localhost:3000/


