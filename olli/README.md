# Olli

This folder contains the deployment information for [Olli](https://github.com/python-discord/olli), our Loki-Discord relay.

The deployment manifest is located within the repository.

A secret called `olli-env` is required and must contain a key `WEBHOOK_URL` with the configured Discord webhook.

The rest of the configuration can be applied through `kubectl apply -f .` in this directory.
