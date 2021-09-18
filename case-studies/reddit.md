[go back](https://github.com/pkardas/learning)

# How Reddit mastered managing growth

*Presentation by Greg Taylor*

330M monthly active users. 8th most popular website in the World. 12M posts per month. 2B votes per month.

Reddit in 2016 - small engineering team with a monolith application. The Infrastructure team was responsible for provisioning and configuring all infrastructure, operating most of systems and handling non-trivial debugging. Static infrastructure. This approach worked for more than a decade. 

In 2016 team started rapidly growing. But monolith application was so fragile, every deploy was an adventure - blocker for the organisation.

How to make everyone's life easier? How to onboard new employees?

Reddit decided to pursue with SOA - Service-Oriented-Architecture. This gave better separation of concerns between teams. However if you have a monolith and it works well for you: "go home, give it a hug, tell it you love it, warts and all".

Growing pains: Automated tests - they started using CI, master branch always had to be green.

Growing pains: Something to build on - instead of copying and pasting services out from another they needed to have a service framework to base off of. Services are configured in the same way, they expose similar set of ports, they have the same async event loop, they fetch secrets the same way, ... - baseplate.readthedocs.io

Growing pains: Artisanal infrastructure - they had hand-crated infrastructure, switched to Terraform (infrastructure as code) - reusable modules - really valuable. Pulling existing infrastructure to Terraform was painful.

Growing pains: Staging/integration woes - their approach for staging was inappropriate for SOA, so they started using Kubernetes.

Growing pains: Infra team as a bottleneck - everything was depending on the infrastructure team, so they gave developers more freedom to modify Terraform. Not all teams want to operate the full stack for their service. 

Service ownership, service owner is empowered to:

- Dev and test their service in a prod-like env
- Do most of the work to get to production
- Own the health of their service
- Diagnose issues

Service ownership comes with some challenges: you need to train developers and still there are mistakes going to happen. Mistakes are learning opportunities.

How to build infrastructure as product? Service owners - learn some Kubernetes basics, deploy and operate their own services. Reddit Infrastructure - Keep the Kubernetes cluster running, provision AWS resources, support and advise Service owners. 

Engineers instead of learning entire stack, had to learn only one technology - Kubernetes. If developer needs eg. S3 - infra engineer is responsible for providing this.

Batteries included - engineers do not have to worry about logging, secrets, security, ... - everything is out of the box.

Extensive documentation and training for developers. Without it you don't have a product, you have a pile of technology.

> An engineer should not require deep infra experience in order to be productive.

Preventing damage: resource limits, throttling, network policy, access controls, scanning for common mistakes, docker image policies
