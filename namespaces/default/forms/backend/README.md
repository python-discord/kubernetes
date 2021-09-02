# Forms Backend

Forms backend is our surveyance system for putting out forms in our community.

This directory contains the necessary routing manifests, the deployment is located in the [python-discord/forms-backend](https://github.com/python-discord/forms-backend) repository.

To create the necessary secret for deployment run:
```bash
$ kubectl create secret generic forms-backend-env \
  --from-literal=DATABASE_URL=<mongodb database url> \
  --from-literal=OAUTH2_CLIENT_ID=<discord oauth2 client id> \
  --from-literal=OAUTH2_CLIENT_SECRET=<discord oauth2 client secret> \
  --from-literal=SECRET_KEY=<session key>
```

Once this has been created, create the deployment with the manifest in the repository and run `kubectl apply -f .` in this directory.
