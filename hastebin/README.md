# Hastebin
These manifests provision an instance of the hastebin service used on paste.pythondiscord.com.

## How to deploy this service
- Check the defaults in `defaults-configmap.yaml` match what you want.
- Create a secret containing your Redis password using:
```bash
$ kubectl create secret generic hastebin-redis-password --from-literal=STORAGE_PASSWORD=<redis password here>
```
- Run `kubectl apply -f .` inside the hastebin folder to provision the ConfigMap, Deployment, Service and Ingress.
