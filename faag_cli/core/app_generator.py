import os
import sys
from time import sleep

from rich import print as rprint
from rich.progress import Progress

from faag_cli.constants import FOLDERS_FILES
from faag_cli.utils import FaagUtils
from faag_cli.utils import templates_environment


class AppGenerator:
    @staticmethod
    def __generate_app(app_type, app_name: str) -> None:
        FaagUtils.handle_app_folder_already_exists()
        if app_type.lower() == "flask":
            rprint(
                "[bold green]🛠 Generating flask app is currently under development. Coming soon...[/bold green]"
            )
            sys.exit(1)
        os.mkdir("app")
        app_template = templates_environment.get_template(f"{app_type}__init__.jinja")
        app_template_rendered = app_template.render(app_name=app_name)
        with open("app/__init__.py", "w", encoding="UTF-8") as fast_api_init:
            fast_api_init.write(app_template_rendered)

    @staticmethod
    def __add_folders_files():
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

    @classmethod
    def gen(cls, app_type: str, app_name: str) -> None:
        with Progress() as progress:
            app_generation = progress.add_task(description="Generating....", total=100)
            sleep(1)
            cls.__generate_app(app_type, app_name)
            progress.update(app_generation, advance=30)
            sleep(1)
            cls.__add_folders_files()
            progress.update(app_generation, advance=40)
            sleep(1)
            FaagUtils.add_gitignore()
            progress.update(app_generation, advance=30)
