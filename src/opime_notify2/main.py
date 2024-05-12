#!/usr/bin/env python3

import click


@click.command()
def main():
    print(f"run main {__name__}")


if __name__ == "__main__":
    main()
