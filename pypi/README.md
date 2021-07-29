# PyPI Server

An instance of [pypi-server](https://github.com/mosquito/pypi-server) used to host packages used in some of our projects.

Alongside the configuration in this directory, a secret named `pypi-auth` is required.

Inside it, an Apache style HTPasswd file should be placed under the key `htpasswd`. This will be used to authorize uploads to the server.
