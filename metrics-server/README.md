# Metrics server

These manifest files provision an instance of the Kubernetes metrics server, used for pod autoscaling, and also for generating resource graphs on the Kubernetes dashboard.

To provision the metrics server run `kubectl apply -f .` in this directory.

You can confirm it has worked by running `kubectl top pods`.
