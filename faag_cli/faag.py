import typer
from rich import print as rprint
from typer import Typer, Option

from faag_cli.core.app_generator import AppGenerator
from faag_cli.utils import FaagUtils

typer_app = Typer()


@typer_app.command(name="generate")
def app_gen(
    app_type: str = Option(
        None,
        "--app-type",
        "-at",
        help="Type of app to generate either flask or fast [default: fast]",
    ),
    app_name: str = Option(
        "sample_app",
        "--app-name",
        "-an",
        help="Name of the app to generate [default: sample_app]",
    ),
):
    FaagUtils.handle_app_folder_already_exists()
    if not app_type:
        rprint(
            "[bold yellow]🧪️Warning: No app type was provided. Falling back to default type [fast][/bold yellow]"
        )
        AppGenerator.gen("fast", app_name)
    if app_type and app_type.lower() not in ["flask", "fast"]:
        rprint(
            "[bold red]:police_car_light:Error: Invalid app type. Please provide valid apptype (fast, flask)[/bold red]"
        )
        typer.Exit(code=1)
    if app_type and app_type.lower() in ["flask", "fast"]:
        AppGenerator.gen(app_type, app_name)


@typer_app.command(name="feature")
def feature_gen():
    rprint("Feature generation is currently under development. Coming soon")


if __name__ == "__main__":
    typer_app()
