# Traefik

This folder contains a `values.yaml` file that is used to provision Python Discord's Traefik ingress controller.

To provision Traefik follow the install instructions at [traefik/traefik-helm-chart](https://github.com/traefik/traefik-helm-chart/tree/master/traefik) and run:
```
helm install -f values.yaml -n kube-system traefik traefik/traefik
```

## Dashboard

The Traefik dashboard can be port forwarded locally at:
 
```
kubectl port-forward -n kube-system $(kubectl get pods -n kube-system --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
```

Then visit http://127.0.0.1:9000/dashboard/
