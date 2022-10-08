import os
import sys
from rich import print as rprint

from faag_cli.utils.templates_loader import templates_environment


class FaagUtils:
    @staticmethod
    def add_gitignore():
        gitignore_template = templates_environment.get_template("gitignore.jinja")
        gitignore_template_rendered = gitignore_template.render()
        with open(".gitignore", "w", encoding="UTF-8") as gitignore:
            gitignore.write(gitignore_template_rendered)

    @staticmethod
    def handle_app_folder_already_exists():
        if os.path.exists("app"):
            rprint(
                "[bold red]:police_car_light:Error: App already exists. Please delete the app folder and try again[/bold red]"
            )
            sys.exit(1)
