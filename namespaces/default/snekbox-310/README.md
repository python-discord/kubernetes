# Snekbox-forms

This folder contains manifests for a Snekbox service that is running Python 3.10.

The deployment manifest for this service is based on in manifest found inside the snekbox repository at [python-discord/snekbox](https://github.com/python-discord/snekbox), modified only by removing the volume mount, 3rd party dep installation script, and hard coding the image version to the most recent 3.10 image on snekbox ghcr.
