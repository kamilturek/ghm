import click

from ghm.fs import OSFileSystem
from ghm.hooks import HooksManager


@click.group()
def cli():
    pass


@cli.command(name="list")
@click.option("-p", "--repository-path")
def list_(repository_path):
    hooks_manager = HooksManager(fs=OSFileSystem())
    for hook in hooks_manager.list_hooks(repository_path):
        click.echo(hook)


@cli.command()
def add():
    pass


if __name__ == "__main__":
    cli()
