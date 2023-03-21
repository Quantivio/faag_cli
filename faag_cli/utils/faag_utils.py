"""
Description: This file contains the FaagUtils class which contains utility methods for the Faag CLI.
"""

import os
import re
import sys
from re import Pattern
from typing import Any

from rich import print as rprint

from faag_cli.utils.templates_loader import templates_environment


class FaagUtils:
    @staticmethod
    def add_gitignore(app_name: str) -> None:
        """
        This method adds a .gitignore file to the project.
        In future this function can be modified to add more config files like .env or .flaskenv to the project.
        :return:
        """
        gitignore_template = templates_environment.get_template("gitignore.jinja")
        gitignore_template_rendered = gitignore_template.render()
        with open(f"{app_name}/.gitignore", "w", encoding="UTF-8") as gitignore:
            gitignore.write(gitignore_template_rendered)

    @staticmethod
    def handle_app_folder_already_exists(app_name: str) -> None:
        """
        This method checks if the app folder already exists and exits the program if it does.
        :return:
        """
        if os.path.exists(app_name):
            rprint(
                "[bold red]:police_car_light:Error: App already exists. Please delete the app folder and try again["
                "/bold red]"
            )
            sys.exit(1)

    @staticmethod
    def validate_app_name(app_name: str) -> str:
        """
        This method validates the app name and returns a validated app name.
        It replaces all hyphens with underscores.

        :param app_name: The name of the app to be generated.
        :return: A validated app name that is safe to use.
        """
        app_name_pattern: Pattern[Any] = re.compile(r".*[@!#$%^&*()<>?/\|}{~:].*")
        if app_name_pattern.match(app_name):
            rprint("[bold red]:police_car_light:Error: App name should not contain special characters[/bold red]")
            sys.exit(1)
        if app_name[0].isdigit():
            rprint("[bold red]:police_car_light:Error: App name should not start with a number[/bold red]")
            sys.exit(1)
        return app_name.replace("-", "_")
