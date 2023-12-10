import click

from app.app import App


@click.command()
@click.option(
    "-c", "--cluster", type=str, help="Name of the AWS ECS cluster", required=True
)
@click.option(
    "-s", "--service", type=str, help="Name of the AWS ECS service", required=True
)
@click.option("-r", "--region", type=str, help="Name of the AWS region", required=True)
def cli(cluster, service, region):
    App(cluster=cluster, service=service, region=region).rollback()
    click.echo(f'Successfully triggered rollback for {service}')
