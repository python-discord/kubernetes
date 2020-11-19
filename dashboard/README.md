# Kubernetes Dashboard
We use an instance of the Kubernetes dashboard to help manage our Kubernetes cluster.

Before starting, ensure that you have deployed the metrics server located in the `metrics-server` folder of this repository.

Once this has been deployed use `kubectl apply -f .` in this directory to create the necessary resources. If you receive an error about a namespace not being defined then run the command again.

To access the dashboard run `kubectl proxy` and visit http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/error?namespace=default (worth bookmarking!)
