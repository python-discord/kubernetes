# Traefik TLS

This set of configuration files sets up the authenticated origin pulls from Cloudflare to ensure all browsing traffic originated from a Cloudflare authenticated server.

## Setup

To set up the authenticated origin pulls, first enable the preference in the Cloudflare Web Dashboard under `SSL/TLS` > `Origin Server`.

Next, create the necessary secret containing the certificate located in `cloudflare-cert.pem` with the following command:

```
$ kubectl create secret -n kube-system generic cloudflare-origin-cert --from-file=tls.ca=cloudflare-cert.pem
```

Next, apply the `tls-option.yaml` manifest to enable authenticated origin pulls at Traefik's end.
