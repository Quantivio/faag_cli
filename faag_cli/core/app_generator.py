import os
import sys

from faag_cli.constants import FOLDERS_FILES
from faag_cli.utils import templates_environment


class AppGenerator:
    @staticmethod
    def generate_app(app, app_name: str) -> None:
        if os.path.exists("app"):
            print("App already exists")
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
