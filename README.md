# ecs-rollback
## _Single command rollback for AWS ECS_

AWS CLI does not provide a native rollback command for ECS deployments. Hence, automating a rollback workflow requires multiple interdependent commands. This is not user-friendly, especially during production outages.

ecs-rollback is tool that solves this problem by allowing users to trigger hassle-free single command rollbacks 

## Prerequisites

ecs-rollback changes the task definition of your service to the (n-1)th task definition. Hence, it is important to note that the tool is effective only when the following ECS best practices are being followed in your CI/CD system:
- Every new deployment should create a new task definition
- Every Docker image linked to task definitions should be tagged with a *unique tag (for e.g. git commit hash)* rather than the *latest* tag

Although AWS does not force users to follow the above two practices, both of them are highly recommended (https://aws.amazon.com/blogs/compute/automating-rollback-of-failed-amazon-ecs-deployments/).

## Installation

```sh
pip install ecs-rollback
```

## Usage

```sh
ecs-rollback -c sample-cluster-name -s sample-service-name -r us-east-1
```
