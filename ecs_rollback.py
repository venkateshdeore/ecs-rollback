import click 

@click.command()
@click.option('-c', '--cluster', type=str, help='Name of the AWS ECS cluster', required=True)
@click.option('-s', '--service', type=str, help='Name of the AWS ECS service', required=True)
@click.option('-r', '--region', type=str, help='Name of the AWS region')
def cli(cluster, service, region):
    click.echo(cluster)
    click.echo(service)
    click.echo(region)
