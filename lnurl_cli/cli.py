import sys
import click

import lnurl

# disable tracebacks on exceptions
sys.tracebacklimit = 0


@click.group()
def command_group():
    """
    LNURL encoding and decoding, enjoy :)"""


@click.command()
@click.argument("string_to_encode", type=str)
def encode(string_to_encode):
    """
    encode as LNURL
    """
    click.echo(lnurl.encode((string_to_encode)))


@click.command()
@click.argument("string_to_decode", type=str)
def decode(string_to_decode):
    """
    encode as LNURL
    """
    click.echo(lnurl.decode((string_to_decode)))


def main():
    command_group.add_command(encode)
    command_group.add_command(decode)
    command_group()


if __name__ == "__main__":
    main()
