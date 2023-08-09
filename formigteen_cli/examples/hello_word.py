from typing import Optional, List
import subprocess
from formigteen_cli.modules.py_inquirer import prompt
from rich import print as rprint
from formigteen_cli import app
import typer
@app.command('hello_world')
def hello_world() -> None:
    typer.echo(f"Hello World!")

@app.command()
def hello(
        description: List[str] = typer.Argument(...),
        quantity: int = typer.Option(1, "--quantity", "-q", min=1, max=10),
) -> None:
    for index in range(quantity):
        rprint("[red bold]Hello[/red bold] [yellow]World[yello]")

@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yello]")

@app.command("list")
def sample_func():
    subprocess.run(f"ls -l", shell=True)


@app.command("create-folder")
def sample_func():
    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'username',
            'message': 'Select any one username: ',
            'choices': [
                {
                    'name': 'Eddie',
                },
                {
                    'name': 'Hughie',
                },
                {
                    'name': 'Matthew ',
                },
                {
                    'name': 'Harvey ',
                },
            ],
        }
    ]

    username = prompt(module_list_question)

    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter folder name :[green bold]")
    folder_name = input()

    subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)
