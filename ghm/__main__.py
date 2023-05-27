import click

from ghm.fs import OSFileSystem
from ghm.hooks import HooksManager


@click.group()
def cli():
    pass


@cli.command(name="list")
def list_():
    hooks_manager = HooksManager(fs=OSFileSystem())
    for hook in hooks_manager.list_hooks(repository_path="sample/"):
        click.echo(hook)


@cli.command()
def add():
    pass


if __name__ == "__main__":
    cli()
