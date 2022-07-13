# Snekbox-forms

This folder contains manifests for a Snekbox service that is running Python 3.11. This instance has the same 3rd party libs installed as the regular snekbox, as of 2022-07-13.

The deployment manifest for this service is based on in manifest found inside the snekbox repository at [python-discord/snekbox](https://github.com/python-discord/snekbox), modified only by removing the volume mount, 3rd party dep installation script, and updating the image path to an image using 3.11 and all deps installed.
