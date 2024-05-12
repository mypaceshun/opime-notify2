#!/usr/bin/env python3

import click


def cli():
    click.echo(f"run hello {__name__}")


if __name__ == "__main__":
    cli()
