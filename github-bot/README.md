# GitHub Bot
The Python Discord GitHub bot watches changes on our GitHub repository to add relevant information such as labels and more to PRs and issues, as well as greeting new contributors.

## Instructions
1. Create the necessary secrets:
``` sh
$ kubectl create secret generic github-bot-secret-env \
  --from-literal=CLIENT_SECRET=<github client secret> \
  --from-literal=SECRET_KEY_BASE=<randomly generated key for sessions> \
  --from-literal=TOKEN=<Personal Access Token (PAT) on github user> \
  --from-literal=WEBHOOK_SECRET=<Secret used for signing webhook payloads>
```
2. Provision the rest of the service with `kubectl apply -f .` in this directory.
3. Deploy the [GitHub Bot](https://github.com/python-discord/github-bot) using the manifest located in the repository.
