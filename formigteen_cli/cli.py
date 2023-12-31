from typing import Optional, List
import typer
import subprocess
from formigteen_cli.modules.py_inquirer import prompt
from rich import print as rprint
from formigteen_cli import __app_name__, __version__, app

import formigteen_cli.examples.hello_word


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return