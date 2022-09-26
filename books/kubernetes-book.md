[go back](https://github.com/pkardas/learning)

# The Kubernetes Book

Book by Nigel Poulton

- [1: Kubernetes primer](#1-kubernetes-primer)

## 1: Kubernetes primer

Kubernetes - an application orchestrator, it orchestrates containerized cloud-native microservices apps.

- orchestrator - a system that deploys and manages applications (dynamically respond to changes - scale up/down,
  self-heal, perform zero-downtime rolling updates)
- containerized app - app that runs in a container - 1980-1990 physical servers era, 2000-2010 virtual machines and
  virtualization era, now cloud-native era
- cloud-native app - designed to meet cloud-like demands of auto-scaling, self-healing, rolling updates, rollbacks and
  more, cloud-native is about the way applications behave and react to events
- microservices app - built from lots of small, specialised, independent parts that work together to form a meaningful
  application

Kubernetes enables 2 things Google and the rest of the industry needs:

1. It abstracts underlying infrastructure such as AWS
2. It makes it easy to move applications on and off clouds

Kubernetes vs Docker Swarm - long story short, Kubernetes won. Docker Swarm is still under active development and is
popular with small companies that need simple alternative to Kubernetes.

Kubernetes as the operating system of the cloud:

- you install a traditional OS on a server, and it abstracts server resources and schedules application processes
- you install Kubernetes on a cloud, and it abstracts cloud resources and schedules application microservices

At a high level, a cloud/datacenter is a pool of compute, network and storage resources. Kubernetes abstracts them.
Servers are no longer pets, they are cattle.

Kubernetes is like a courier service - you package the app as a container, give it a Kubernetes manifest, and let
Kubernetes take care of deploying it and keeping it running. 
