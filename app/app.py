import boto3


class App:
    def __init__(self, **kwargs):
        self.region = kwargs.get("region")
        self.service = kwargs.get("service")
        self.cluster = kwargs.get("cluster")
        self.client = boto3.client("ecs", self.region)

    def fetch_latest_task_definition(self):
        service_description = self.client.describe_services(
            cluster=self.cluster, services=[self.service]
        )
        return service_description["services"][0]["taskDefinition"]

    def generate_rollback_task_definition(self, latest_task_definition):
        latest_task_definition_version = int(latest_task_definition.split(":")[-1])
        rollback_task_definition_version = latest_task_definition_version - 1
        if rollback_task_definition_version <= 0:
            raise Exception(
                "Rollback is not possible as the task definition version is invalid"
            )
        task_definition_prefix = ":".join(latest_task_definition.split(":")[:-1])
        rollback_task_definition = (
            f"{task_definition_prefix}:{rollback_task_definition_version}"
        )
        return rollback_task_definition

    def deploy_task_definition(self, task_definition):
        self.client.update_service(
            cluster=self.cluster, service=self.service, taskDefinition=task_definition
        )

    def rollback(self):
        latest_task_definition = self.fetch_latest_task_definition()
        rollback_task_definition = self.generate_rollback_task_definition(
            latest_task_definition
        )
        self.deploy_task_definition(rollback_task_definition)
