# -*- coding: utf-8 -*-

"""Console script for shenko."""

import click

@click.command()
def main(args=None):
    """Console script for shenko."""
    click.echo("click starting shenko app")
    click.launch("shenko.py")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
