"""
Description: This file contains the AppGenerator class which is responsible for generating the app.
"""
import os
import subprocess

from rich import print as rprint
from rich.progress import Progress

from faag_cli.constants.constants import FOLDERS_FILES
from faag_cli.utils.faag_utils import FaagUtils
from faag_cli.utils.poetry_template_generator import generate_poetry_template
from faag_cli.utils.templates_loader import templates_environment


class AppGenerator:
    def __init__(self, app_name: str, app_type: str, linter: str, formatter: str) -> None:
        """
        :param app_name: The name of the app to be generated.
        :param app_type: The type of the app to be generated.
        :param linter: The linter to be used for the project.
        """
        self.app_name = app_name
        self.app_type = app_type
        self.linter = linter
        self.formatter = formatter

    def __generate_app(self) -> None:
        # Create the app folder
        os.mkdir(f"{self.app_name}/app")

        # Generate the base __init__.py file for respective app via the templates loader
        app_template = templates_environment.get_template("/base/__init__.jinja")
        app_template_rendered = app_template.render(app_name=self.app_name, app_type=self.app_type)
        with open(f"{self.app_name}/app/__init__.py", "w", encoding="UTF-8") as init_file:
            init_file.write(app_template_rendered)

    def __add_folders_files(self) -> None:
        """
        This method adds the folders and files to the app folder based on the FOLDERS_FILES structure.
        :return:
        """
        if not os.path.exists(f"{self.app_name}/app/schemas"):
            os.mkdir(f"{self.app_name}/app/schemas")

        for folder, files in FOLDERS_FILES.items():
            if folder in ["response", "request"]:
                os.mkdir(f"{self.app_name}/app/schemas/{folder}")
                for file in files:
                    with open(
                        f"{self.app_name}/app/schemas/{folder}/{file}.py",
                        "w",
                        encoding="UTF-8",
                    ) as gen_file:
                        if file.startswith("__"):
                            template = templates_environment.get_template(f"/schemas/{folder}/{folder + file}.jinja")
                        else:
                            template = templates_environment.get_template(f"/schemas/{folder}/{file}.jinja")
                        rendered_template = template.render(app_type=self.app_type)
                        gen_file.write(rendered_template)
            else:
                if folder != "schemas":
                    os.mkdir(f"{self.app_name}/app/{folder}")
                for file in files:
                    with open(f"{self.app_name}/app/{folder}/{file}.py", "w", encoding="UTF-8") as gen_file:
                        if file.startswith("__"):
                            template = templates_environment.get_template(f"/{folder}/{folder + file}.jinja")
                        else:
                            template = templates_environment.get_template(f"/{folder}/{file}.jinja")
                        rendered_template = template.render(app_type=self.app_type)
                        gen_file.write(rendered_template)

    def setup_poetry(self) -> None:
        """
        This method sets up poetry for the project.
        :return: None
        """
        os.mkdir(self.app_name)

        # Setup Poetry
        generated_template = generate_poetry_template(
            self.app_name,
            self.app_type,
            self.linter,
            self.formatter,
        )
        with open(f"{self.app_name}/pyproject.toml", "w", encoding="UTF-8") as poetry_file:
            poetry_file.write(generated_template)
        subprocess.run(f"cd {self.app_name} && poetry install", shell=True, capture_output=True)
        rprint("[bold green]🎉Poetry setup complete! [/bold green]")

    def gen(self) -> None:
        # Progress bar for user experience
        with Progress() as progress:
            # Since app doesn't does so much heavy lifting, we can use a simple progress bar to simulate the progress.

            app_generation = progress.add_task(description="⌛️Generating....", total=100)

            # Setup Poetry
            progress.update(app_generation, advance=5)
            self.setup_poetry()
            progress.update(app_generation, advance=35)

            # Generate the app
            self.__generate_app()
            progress.update(app_generation, advance=20)

            # Add folders and files
            self.__add_folders_files()
            progress.update(app_generation, advance=20)

            # Add other files like .gitignore, .env, .flaskenv
            FaagUtils.add_other_files(self.app_name, self.app_type)
            progress.update(app_generation, advance=20)
