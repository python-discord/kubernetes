# Grafana

This folder contains the manifests for deploying our Grafana instance, the service we use to query our data.

To deploy it create a secret with all the secret variables like so:

```
kubectl create secret generic grafana-secret-env \
  --from-literal=GF_SECURITY_ADMIN_PASSWORD=<admin password> \
  --from-literal=GF_AUTH_GITHUB_CLIENT_ID=<github client id> \
  --from-literal=GF_AUTH_GITHUB_CLIENT_SECRET=<github client secret>
```

Then, apply the rest of the manifests by running `kubectl apply -f .` in this folder.
