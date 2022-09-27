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

Worker nodes - are where user applications run. At a high-level they do 3 things:

1. Watch the API server for new work assignments
2. Execute work assignments
3. Report back to the control plane (via the API server)

3 major components:

1. Kubelet - main Kubernetes agent and runs on every worker node. Watches the API server for new work tasks. Executes
   the task and maintains reporting channel back to the control plane.
2. Container runtime - kubelet needs it to perform container-related tasks - things like pulling images and starting and
   stopping containers.
3. Kube-proxy - runs on every node and is responsible for local cluster networking.

In order to run on a Kubernetes cluster an application needs to:

1. Be packaged as a container
2. Be wrapped in a Pod
3. Be deployed via a declarative manifest file

The declarative model:

- declare the desired state of an application microservice in a manifest file
    - desired state - image, how many replicas, which network ports, how to perform updates
- post it to the API server
    - using `kubectl` CLI (it uses a HTTP request)
- Kubernetes stores it in the cluster store as the application's desired state
- Kubernetes implements the desired state on the cluster
- A controller makes sure the observed state of the application doesn't vary from the desired state
    - background reconciliation loops that constantly monitor the state of the cluster, if desired state != observed
      state - Kubernetes performs the necessary tasks

Kubernetes Pod - a wrapper that allows a container to run on a Kubernetes cluster. Atomic unit of scheduling. VMware has
virtual machines, Docker has containers, Kubernetes has Pods. In Kubernetes, every container must run inside a Pod. "
Pod" comes from "a pod of whales" (group of whales is called "a pod of whales"). "Pod" and "container" are often used
interchangeably, however it is possible (in some advanced use-cases) to run multiple containers in a single Pod.

Pods don't run applications - applications always run in containers, the Pod is just a sandbox to run one or more
containers. Pods are also the minimum unit of scheduling in Kubernetes. If you need to scale an app, you add or remove
Pods. You do not scale by adding more containers to existing Pods.

A pod is only ready for service when all its containers are up and running. A single Pod can only be scheduled to a
single node.

Pods are immutable. Whenever we talk about updating Pods, we mean - delete and replace it with a new one. Pods are
unreliable.

Example controller: Deployments - a high-level Kubernetes object that wraps around a Pod and adds features such as
self-healing, scaling, zero-downtime rollouts, and versioned rollbacks.

Services - provide reliable networking for a set of Pods. Services have a stable DNS name, IP address and name, they
load-balance traffic across a dynamic set of Pods. As Pods come and go, the Service observes this, automatically updates
itself, and continues to provide that stable networking endpoint.

Service - a stable network abstraction that provides TCP/UPD load-balancing across a dynamic set of Pods.
