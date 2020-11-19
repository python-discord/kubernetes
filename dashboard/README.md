# Kubernetes Dashboard
We use an instance of the Kubernetes dashboard to help manage our Kubernetes cluster.

First, add the Helm repo we will be using:
```
$ helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
```

Next, create a deployment of the dashboard:
```
$ helm install -f values.yaml dashboard kubernetes-dashboard/kubernetes-dashboard --namespace kube-system
```

Then, proxy the dashboard locally using:
```
$ kubectl -n kube-system port-forward deployment/dashboard-kubernetes-dashboard 8443:8443
```

Access the dashboard through https://localhost:8443/. You will be asked for a Kubernetes Configuration file to authenticate with.
