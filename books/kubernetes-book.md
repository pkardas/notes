[go back](https://github.com/pkardas/learning)

# The Kubernetes Book

Book by Nigel Poulton, https://github.com/nigelpoulton/TheK8sBook

- [1: Kubernetes primer](#1-kubernetes-primer)
- [2: Kubernetes principles of operation](#2-kubernetes-principles-of-operation)
- [3: Getting Kubernetes](#3-getting-kubernetes)
- [4: Working with Pods](#4-working-with-pods)

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

## 3: Getting Kubernetes

Hosted Kubernetes: AWS Elastic Kubernetes Service, Google Kubernetes Engine, Azure Kubernetes Service. Managing your own
Kubernetes cluster isn't a good use of time and other resources. However, it is easy to rack up large bills if you
forget to turn off infrastructure when not in use.

The hardest way to get a Kubernetes cluster is to build it yourself.

Play with Kubernetes - quick and simple way to get your hands on a development Kubernetes cluster. However, it is time
limited and sometimes suffers from capacity and performance issues. Link: https://labs.play-with-k8s.com

Docker Desktop - offers a single-node Kubernetes cluster that you can develop and test with.

`kubectl` is the main Kubernetes command-line tool. At a high-level, `kubectl` converts user-friendly commands into HTTP
REST requests with JSON content required by the Kubernetes API server.

```shell
kubectl get nodes
```

```shell
kubectl config current-context
```

```shell
kubectl config use-context docker-desktop
```

## 4: Working with Pods

Controllers - infuse Pods with super-powers such as self-healing, scaling, rollouts and rollbacks. Every Controller bas
a PodTemplate defining the Pods it deploys and manages. You rarely interact with Pods directly.

Pod - the atomic unit of scheduling in Kubernetes. Apps deployed to Kubernetes always run inside Pods. If you deploy an
app, you deploy it in a Pod. If you terminate an app, you terminate its Pod. If you scale your app up/down, you
add/remove Pods.

Kubernetes doesn't allow containers to run directly on a cluster, they always have to be wrapped in a Pod.

1. Pods augment containers

- labels - group Pods and associate them with others
- annotations - add experimental features and integrations with 3rd-party tools
- probes - test the health and status of Pods and the apps they run, this enables advanced scheduling, updates, and
  more.
- affinity and anti-affinity rules - control over where in the cluster Pods are allowed to run
- termination controls - gracefully terminate Pods and the apps they run
- security policies - enforce security features
- resource requests and limits - min. and max. values for CPU, memory, IO, ...

Despite bringing so many features, Pods are super-lightweight and add very little overhead.

```shell
kubectl explain pods --recursive
```

```shell
kubectl explain pod.spec.restartPolicy
```

2. Pods assist in scheduling

Every container in a Pods is guaranteed to be scheduled to the same worker node.

3. Pods enable resource sharing

Pods provide a shared execution environment for one or more containers (filesystem, network stack, memory, volumes). So
if a Pod has 2 containers, both containers share the Pod's IP address and can access ony of the Pod's volumes to share
data.

There are 2 ways to deploy a Pod:

- directly via a Pod manifest
    - called "Static Pods", no super-powers like self-healing, scaling, or rolling updates
- indirectly via a controller
    - have all the benefits of being monitored by a highly-available controller running on the control-plane

Pets vs Cattle paradigm - Pods are cattle, when they die, they get replaced by another. The old one is gone, and a shiny
new one (with the same config, but a different IP and UID) magically appears and takes its place.

This is why applications should always store state and data outside the Pod. It is also why you should not rely on
individual Pods - they are ephemeral, here today, gone tomorrow.

Deploying Pods:

1. Define it in a YAML manifest file
2. Post it to the API server
3. The API server authenticates and authorizes the request
4. The configuration (YAML) is validated
5. The scheduler deploys the Pod to a healthy worker node with enough available resources

If you are using Docker or containerd as your container runtime, a Pod is actually a special type of container - a pause
container. This means containers running inside of Pods are really containers running inside containers.

The Pod Network is flat, meaning every Pod can talk directly to every other Pod without the need for complex routing and
port mappings. You should use Kubernetes Network Policies.

Pod deployment is an atomic operation - all-or-nothing - deployment either succeeds or fails. You will never have a
scenario where a partially deployed Pod is servicing requests.

Pod lifecycle: pending -> running (long-lived Pod) | succeeded (short-lived Pod)

- short-lived - batch jobs, designed to only run until a task completes
- long-lived - web-servers, remain in the running phase indefinitely, if container fail, the controller may attempt to
  restart them

Pods are immutable objects. You can't modify them after they are deployed. You always replace a Pod with a new one (in
case of a failure or update).

If you need to scale an app, you add or remove Pods (horizontal scaling). You never scale an app by adding more of the
same containers to a Pod. Multi-container Pods are only for co-scheduling and co-locating containers that need tight
coupling.

Co-locating multiple containers in the same Pod allows containers to be designed with a single responsibility but
co-operate closely with others.

Kubernetes multi-container Pod patterns:

- Sidecar pattern - (most popular) the job of a sidecar is to augment of perform a secondary task for the main
  application container
- Adapter pattern - variation of the sidecar pattern where the helper container takes non-standardized output from the
  main container and rejigs it into a format required by an external system
- Ambassador pattern - variation of the sidecar pattern where the helper container brokers connectivity to an external
  system, ambassador containers interface with external systems on behalf of the main app container
- Init pattern - runs a special init container that is guaranteed to start and complete before your main app container,
  it is also guaranteed to run only once

```shell
kubectl get pods
```

Get pods info with additional info:

```shell
kubectl get pods -o wide
```

Get pod info, a full copy of the Pod from the cluster:

```shell
kubectl get pods -o yaml
```

Get even more info; spec - desired state, status - observed state:

```shell
kubectl get pods hello-pod -o yaml
```

Pod manifest files:

- kind - tells the Kubernetes the type of object being defined
- apiVersion - defines the schema version to use when creating the object
- metadata - names, labels, annotations, and a Namespace
- spec - define the containers the Pod will run

```shell
kubectl apply -f pod.yml
```

`kubectl describe` - a nicely formatted multi-line overview of an object: You can add the `--watch` flag to the command
to monitor it and see when the status changes to _Running_.

```shell
kubectl describe pods hello-pod
```

You can see ordering and names of containers using this command.

`kubectl logs` - like other Pod related commands, if you don't specify `--container`, it executes against the first
container in the pod:

```shell
kubectl logs hello-pod
```

```shell
kubectl logs hello-pod --container hello-ctr
```

`kubectl exec` - execute commands inside a running Pod

```shell
kubectl exec hello-pod -- pwd
```

Get shell access:

```shell
kubectl exec -it hello-pod hello-pod -- sh
```

`-it` flag makes the session interactive and connects STDIN and STDOUT on your terminal to STD and STDOUT inside the
first container in teh Pod.

Pod hostname - every container in a Pod inherits its hostname from the name of the Pod (`metadata.name`). With this in
mind, you should always set Pod names as valid DNS names (a-z, 0-9, +, -, .).

`spec.initCointainers` block defines one or more containers that Kubernetes guarantees will run and complete before main
app container starts.

```shell
kubectl delete pod git-sync
```
