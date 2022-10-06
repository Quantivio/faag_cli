import os

from typer import run

from faag_cli.constants import FOLDERS_FILES
from faag_cli.utils import templates_environment


class Faag:
    @staticmethod
    def generate_app() -> None:
        os.mkdir("app")
        fast_template = templates_environment.get_template("fast_api__init__.jinja")
        fast_template_rendered = fast_template.render()
        with open("app/__init__.py", "w", encoding="UTF-8") as fast_api_init:
            fast_api_init.write(fast_template_rendered)

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


def faag_cli():
    faag = Faag()
    faag.add_gitignore()
    faag.generate_app()
    faag.add_folders_files()
    faag.add_packages()


if __name__ == "__main__":
    run(faag_cli)
