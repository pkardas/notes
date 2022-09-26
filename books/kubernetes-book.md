[go back](https://github.com/pkardas/learning)

# The Kubernetes Book

Book by Nigel Poulton

- [1: Kubernetes primer](#1-kubernetes-primer)
- [2: Kubernetes principles of operation](#2-kubernetes-principles-of-operation)

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

## 2: Kubernetes principles of operation

Kubernetes is 2 things:

- a cluster to run applications on
    - like any cluster - bunch od machines to host apps
    - these machines are called "nodes" (physical servers, VMs, cloud instances, Raspberry PIs, ...)
    - cluster is made of:
        - control plane (the brains) - exposes the API, has a scheduler for assigning work, records the state of the
          cluster and apps
        - worker nodes (the muscle) - where user apps run
- an orchestrator of cloud-native microservices apps
    - a system that takes care of deploying and managing apps

Simple process to run apps on a Kubernetes cluster:

1. Design and write the application as small independent microservices
2. Package each microservice as its own container
3. Wrap each container in a Kubernetes Pod
4. Deploy Pods to the cluster via higher-level controllers such as Deployments, DaemonSets, StatefulSets, CronJobs, ...

The Control Plane - runs a collection of system services that make up the control plane of the cluster (Master, Heads,
Head nodes). Production envs should have multiple control plane nodes - 3 or 5 recommended, and should be spread across
availability zones. Different services making up the control plane:

- The API server - the Grand Central station of Kubernetes, all communication, between all components, must go through
  the API server. All roads lead to the API Server.
- The Cluster Store - the only stateful part of the Control Plane, stores the configuration and the state. Based
  on `etcd` (a popular distributed database).
- The Controller Manager and Controllers - all the background controllers that monitor cluster components amd respond to
  events.
- The Scheduler - watches the API server for new work tasks and assigns them to appropriate healthy worker nodes. Only
  responsible for picking the nodes to run tasks, it isn't responsible for running them.
- The Cloud Controller Manager - its job is to facilitate integrations with cloud services, such as instances,
  load-balancers, and storage.
