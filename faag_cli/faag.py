"""
Description: This file contains the main entry point for the Faag CLI.
"""

import typer
from rich import print as rprint
from typer import Option, Typer

from faag_cli.constants.app_types import AppTypes
from faag_cli.core.app_generator import AppGenerator
from faag_cli.utils.faag_utils import FaagUtils

typer_app = Typer()  # Create a Typer instance


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
) -> None:
    """
    FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI.
    """
    FaagUtils.handle_app_folder_already_exists(app_name)  # Check if the app folder already exists
    app_type = app.value.lower()  # Get the app type
    if not app_type:
        rprint("[bold yellow]🧪️Warning: No app type was provided. Falling back to default type [fast][/bold yellow]")
        AppGenerator.gen("fast", app_name)

    # Check if the app type is valid
    if app_type and app_type not in ["flask", "fast"]:
        rprint(
            "[bold red]:police_car_light:Error: Invalid app type. Please provide valid app type (fast, flask)[/bold "
            "red]"
        )
        typer.Exit(code=1)

    if app_type and app_type in ["flask", "fast"]:
        # App generation starts here
        AppGenerator.gen(app_type, app_name)


@typer_app.command(name="feature")
def feature_gen() -> None:
    rprint("Feature generation is currently under development. Coming soon")


@typer_app.command(name="version")
def version() -> None:
    """
    Prints the version of Faag CLI
    """
    rprint("Faag CLI version 0.0.3-dev0")


if __name__ == "__main__":
    typer_app()
