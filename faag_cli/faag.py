"""
Description: This file contains the main entry point for the Faag CLI.
"""

import typer
from rich import print as rprint
from typer import Option, Typer

from faag_cli.constants.app_enums import AppTypes, FormatterTypes, LinterTypes
from faag_cli.core.app_generator import AppGenerator
from faag_cli.utils.faag_utils import FaagUtils

__version__ = "0.2.1"

typer_app = Typer(
    name="Faag CLI",
    help="FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI.",
)  # Create a Typer instance


@typer_app.command(name="generate")
def app_gen(
    app: AppTypes = Option(
        AppTypes.FAST.value,
        "--type",
        "-t",
        help="Type of app to generate either flask or fast [default: fast]",
        show_choices=True,
        prompt="What type of app do you want to generate?",
    ),
    app_name: str = Option(
        "sample_app",
        "--name",
        "-n",
        help="Name of the app to generate [default: sample_app]",
        prompt="What is the name of your app? [default: sample_app]",
    ),
    linter: LinterTypes = Option(
        LinterTypes.RUFF.value,
        "--linter",
        "-l",
        help="Linter to use for the app [default: ruff]",
        show_choices=True,
        prompt="What linter do you want to use?",
    ),
    formatter: FormatterTypes = Option(
        FormatterTypes.BLACK.value,
        "--formatter",
        "-f",
        help="Formatter to use for the app [default: black]",
        show_choices=True,
        prompt="What formatter do you want to use?",
    ),
) -> None:
    """
    FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI.
    """
    FaagUtils.handle_app_folder_already_exists(app_name)  # Check if the app folder already exists
    app_type = app.value.lower()  # Get the app type

    # Validate the app name
    validated_app_name: str = FaagUtils.validate_app_name(app_name)

    # Check if the app type is valid
    if app_type and app_type not in ["flask", "fast"]:
        rprint(
            "[bold red]:police_car_light:Error: Invalid app type. Please provide valid app type (fast, flask)[/bold "
            "red]"
        )
        typer.Exit(code=1)

    if app_type and app_type in ["flask", "fast"]:
        # App generation starts here
        app_generator: AppGenerator = AppGenerator(
            app_type=app_type,
            app_name=validated_app_name,
            linter=linter.value.lower(),
            formatter=formatter.value.lower(),
        )
        app_generator.gen()


@typer_app.command(name="feature")
def feature_gen() -> None:
    rprint("Feature generation is currently under development. Coming soon")


def version_callback(value: bool):
    if value:
        rprint(f"Faag CLI version: [bold green]{__version__}[/bold green]")
        raise typer.Exit()


@typer_app.callback()
def version(
    version_arg: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Prints the version of Faag CLI",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """
    Prints the version of Faag CLI
    """
    pass


if __name__ == "__main__":
    typer_app()
