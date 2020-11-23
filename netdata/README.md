# Netdata

This folder contains a `values.yaml` file that is used to provision Python Discord's Netdata.

To provision Netdata run the following helm commands to install the service:
```
helm repo add netdata https://netdata.github.io/helmchart/
helm install -f values.yaml -n kube-system netdata netdata/netdata
```

Once this is done, run the following to apply the relevant service and ingress manifests:
```
kubectl apply -f manifests
```
