# paste.pythondiscord.com
These manifests provision an instance of the hastebin service used on paste.pythondiscord.com.

## How to deploy this service
- Edit the `init.sh` to specify the storage type, host and password
- Run `kubectl create configmap hastebin-init --from-file=init.sh` to create the required **ConfigMap**
- Revert the changes on `init.sh` - **We don't want to commit anything sensitive!**
- Run `kubectl apply -f .`
