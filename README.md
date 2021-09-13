# Kubernetes
Configuration and [documentation](https://python-discord.github.io/kubernetes/)
for Python Discord's Kubernetes setup!


# How to create secrets
Many of these deployments require you to create secret environments. These are not in this repository, for security reasons, so you need to manually create them.

The easiest way to do this is to use `kubectl create secret`. For example:

```shell script
kubectl create secret generic new-secret-env \
  --from-literal=MY_FAVORITE_THING=lemons \
  --from-literal=SUPER_LAME_DOG=snoopy
```

It's also possible to create a secret manifest file, but **make sure not to commit it!**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
stringData:
  KEY: "value"
```
