---
title: Kubespray Deployment
layout: page
---

## Bootstrap

1. Follow Debian [installation notes](https://kubespray.io/#/docs/debian)
1. Add a public key for `hopper` on to each node, so it can passwordless ssh
1. Change hopper in `inventory/host.yaml` to be `127.0.0.1`
1. Run our ansible roles
   1. Create a virtual environment on `hopper` and install requirements from `infra/requirements.txt`
   1. `ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbook.yaml -i inventory/hosts.yaml -u root`
1. Run kubespray
   1. Create a virtual environment on `hopper` and install requirements from `infra/kubespray/requirements-2.12.txt`
   1. `ANSIBLE_CONFIG=ansible.cfg ansible-playbook  kubespray/cluster.yaml -i inventory/hosts.yaml -u root`
   1. NOTE: Can we remove the `localhost` roles?

## Kubernetes

1. Using CEPH RDB volume provisioner && Using Rook for K8s volume claim intergration
