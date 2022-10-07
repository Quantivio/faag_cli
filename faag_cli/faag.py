from typer import Typer, Option

from faag_cli.core import AppGenerator

typer_app = Typer()


@typer_app.command(
    name="Faag_CLI",
    help="Generate a new FastAPI/Flask project",
)
def generate(
    app_type: str = Option(
        "fast_api",
        "--app",
        "-a",
        help="Type of that should be generated. Default type is fast_api. Valid Options are: [fast_api, flask]",
    ),
    app_name: str = Option(
        "sampel_app",
        "--app-name",
        "-an",
        help="Name of the app",
    ),
) -> None:
    faag = AppGenerator()
    faag.add_gitignore()
    faag.generate_app(app_type, app_name)
    faag.add_folders_files()
    faag.add_packages()


if __name__ == "__main__":
    typer_app()
