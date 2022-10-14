import os
from time import sleep

from rich.progress import Progress

from faag_cli.constants import FOLDERS_FILES
from faag_cli.utils import FaagUtils
from faag_cli.utils import templates_environment


class AppGenerator:
    @staticmethod
    def __generate_app(app_type, app_name: str) -> None:
        validated_app_name: str = FaagUtils.validate_app_name(app_name)
        os.mkdir("app")
        app_template = templates_environment.get_template("__init__.jinja")
        app_template_rendered = app_template.render(
            app_name=validated_app_name, app_type=app_type
        )
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
            app_generation = progress.add_task(
                description="⌛️Generating....", total=100
            )
            sleep(0.5)
            cls.__generate_app(app_type, app_name)
            progress.update(app_generation, advance=30)
            sleep(0.5)
            cls.__add_folders_files()
            progress.update(app_generation, advance=40)
            sleep(0.5)
            FaagUtils.add_gitignore()
            progress.update(app_generation, advance=30)
