"""
Description: This file contains the AppGenerator class which is responsible for generating the app.
"""
import os
from time import sleep

from rich.progress import Progress

from faag_cli.constants.constants import FOLDERS_FILES
from faag_cli.utils.faag_utils import FaagUtils
from faag_cli.utils.templates_loader import templates_environment


class AppGenerator:
    @staticmethod
    def __generate_app(app_type: str, app_name: str) -> None:
        """
        :param app_type: The type of the app to be generated, either fast or flask.
        :param app_name: The name of the project or app to be generated.
        :return: None
        """

        # Validate the app name
        validated_app_name: str = FaagUtils.validate_app_name(app_name)

        # Create the app folder
        os.mkdir("app")

        # Generate the base __init__.py file for respective app via the templates loader
        app_template = templates_environment.get_template("/base/__init__.jinja")
        app_template_rendered = app_template.render(app_name=validated_app_name, app_type=app_type)
        with open("app/__init__.py", "w", encoding="UTF-8") as fast_api_init:
            fast_api_init.write(app_template_rendered)

    @staticmethod
    def __add_folders_files(app_type: str) -> None:
        """
        This method adds the folders and files to the app folder based on the FOLDERS_FILES structure.
        :param app_type: The type of the app to be generated, either fast or flask.
        :return:
        """
        if not os.path.exists("app/schemas"):
            os.mkdir("app/schemas")

        for folder, files in FOLDERS_FILES.items():
            if folder in ["response", "request"]:
                os.mkdir(f"app/schemas/{folder}")
                for file in files:
                    with open(f"app/schemas/{folder}/{file}.py", "w", encoding="UTF-8") as gen_file:
                        if file.startswith("__"):
                            template = templates_environment.get_template(f"/schemas/{folder}/{folder + file}.jinja")
                        else:
                            template = templates_environment.get_template(f"/schemas/{folder}/{file}.jinja")
                        rendered_template = template.render(app_type=app_type)
                        gen_file.write(rendered_template)
            else:
                if folder != "schemas":
                    os.mkdir(f"app/{folder}")
                for file in files:
                    with open(f"app/{folder}/{file}.py", "w", encoding="UTF-8") as gen_file:
                        if file.startswith("__"):
                            template = templates_environment.get_template(f"/{folder}/{folder + file}.jinja")
                        else:
                            template = templates_environment.get_template(f"/{folder}/{file}.jinja")
                        rendered_template = template.render(app_type=app_type)
                        gen_file.write(rendered_template)

    @staticmethod
    def setup_poetry(app_name: str, app_type: str) -> None:
        """
        This method sets up poetry for the project.
        :return: None
        """
        os.system(f"poetry init -n {app_name} -q")
        os.system("poetry add pydantic")
        os.system("poetry add python-dotenv")
        os.system("poetry add ruff")
        os.system("poetry add pytest")
        if app_type == "fast":
            os.system("poetry add fastapi")
            os.system("poetry add uvicorn")
        else:
            os.system("poetry add flask")

    @classmethod
    def gen(cls, app_type: str, app_name: str) -> None:
        # Progress bar for user experience
        with Progress() as progress:
            # Since app doesn't does so much heavy lifting, we can use a simple progress bar and sleep for 0.5
            # seconds to simulate the progress.
            app_generation = progress.add_task(description="⌛️Generating....", total=100)
            sleep(0.5)
            cls.__generate_app(app_type, app_name)
            progress.update(app_generation, advance=20)
            sleep(0.5)
            cls.__add_folders_files(app_type)
            progress.update(app_generation, advance=20)
            sleep(0.5)
            FaagUtils.add_gitignore()
            progress.update(app_generation, advance=20)
            sleep(0.5)
            cls.setup_poetry(app_name, app_type)
            progress.update(app_generation, advance=40)
