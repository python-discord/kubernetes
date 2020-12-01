# Redirects
Some of our point to an external service, for example https://git.pythondiscord.com/ points towards our GitHub organisation.

This folder contains all the redirects for our subdomains.

They consist of a Traefik Middleware to handle the redirection and a Traefik IngressRoute to bring traffic into the cluster.

To deploy these routes simply run `kubectl apply -f .` in this folder.
