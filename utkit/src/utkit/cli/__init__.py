import typer
from importlib.metadata import version as get_version

app = typer.Typer(no_args_is_help=True, help="utkit - core libraries for development.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"utkit v{get_version('utkit')}")
        raise typer.Exit()


@app.callback()
def callback(
    version: bool = typer.Option(
        None,
        "--version",
        callback=_version_callback,
        is_eager=True,
        help="Show version and exit.",
    ),
) -> None:
    pass


@app.command()
def version() -> None:
    """Show the current version of utkit."""
    typer.echo(f"utkit v{get_version('utkit')}")


def main() -> None:
    app()
