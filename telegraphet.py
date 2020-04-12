#!/usr/bin/env python3.8
import json
import os
import sys
from typing import Final

import typer
from telegraph import Telegraph


def auth_token() -> str:
    token = os.environ.get('TELEGRAPH_TOKEN')
    if token is None:
        try:
            f = open(os.path.expanduser('~/.config/telegraphet/config.json'))
        except OSError:
            typer.echo("Telegra.ph access token not found!\nRun `telegraphet --init` to create a new one.")
        else:
            with f:
                config = json.load(f)
                return config['token']
    else:
        return token


def create_page(title: str, content: str) -> str:
    token: str = auth_token()
    telegraph: Final[Telegraph] = Telegraph(token)
    page = telegraph.create_page(title, html_content=content)
    return page['url']


def create_account(username: str):
    telegraph: Final[Telegraph] = Telegraph()
    telegraph.create_account(username)


def main(title: str, init: str = typer.Option("", help="username", prompt=True)):
    if init:
        create_account(init)
    else:
        typer.echo(create_page(title, sys.stdin.read()))


if __name__ == "__main__":
    typer.run(main)