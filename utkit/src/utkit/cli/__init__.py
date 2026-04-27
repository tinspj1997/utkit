import subprocess
from pathlib import Path

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


@app.command()
def docs() -> None:
    """Serve the utkit documentation locally on port 8005 and open in browser."""
    docs_dir = Path(__file__).parent.parent / "documentation"
    if not docs_dir.exists():
        typer.echo(f"Documentation folder not found: {docs_dir}", err=True)
        raise typer.Exit(code=1)

    typer.echo("Starting docs server at http://localhost:8005 ...")
    subprocess.run(
        ["zensical", "serve", "--dev-addr", "localhost:8005", "--open"],
        cwd=docs_dir,
        check=True,
    )


def main() -> None:
    app()
