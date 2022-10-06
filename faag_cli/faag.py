import os
import sys

import typer
from typer import Typer, Option

from faag_cli.constants import FOLDERS_FILES
from faag_cli.utils import templates_environment

typer_app = Typer()


class Faag:
    @staticmethod
    def generate_app(app, app_name: str) -> None:
        if os.path.exists("app"):
            typer.echo("App already exists")
            sys.exit(1)
        if app not in ["fast_api", "flask"]:
            raise ValueError(
                "Invalid app type. Please provide valid arguments [fast_api, flask]"
            )
        if app == "flask":
            print("Generating flask app is currently under development. Please wait")
            sys.exit(1)
        os.mkdir("app")
        app_template = templates_environment.get_template(f"{app}__init__.jinja")
        app_template_rendered = app_template.render(app_name=app_name)
        with open("app/__init__.py", "w", encoding="UTF-8") as fast_api_init:
            fast_api_init.write(app_template_rendered)

    @staticmethod
    def add_gitignore():
        gitignore_template = templates_environment.get_template("gitignore.jinja")
        gitignore_template_rendered = gitignore_template.render()
        with open(".gitignore", "w", encoding="UTF-8") as gitignore:
            gitignore.write(gitignore_template_rendered)

    @staticmethod
    def add_packages():
        print("Adding packages....")

    @staticmethod
    def add_folders_files():
        for folder, files in FOLDERS_FILES.items():
            os.mkdir(f"app/{folder}")
            for file in files:
                with open(f"app/{folder}/{file}.py", "w", encoding="UTF-8") as gen_file:
                    if file.startswith("__"):
                        template = templates_environment.get_template(
                            f"{folder + file}.jinja"
                        )
                    else:
                        template = templates_environment.get_template(f"{file}.jinja")
                    rendered_template = template.render()
                    gen_file.write(rendered_template)


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
    app_name: str = Option("sampel_app", "--app-name", "-an", help="Name of the app"),
) -> None:
    faag = Faag()
    faag.add_gitignore()
    faag.generate_app(app_type, app_name)
    faag.add_folders_files()
    faag.add_packages()


if __name__ == "__main__":
    typer_app()
