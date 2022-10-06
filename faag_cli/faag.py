import os

from faag_cli.constants import FOLDERS_FILES
from utils.templates_loader import templates_environment


class Faag:
    @staticmethod
    def generate_app() -> None:
        os.mkdir("app")
        fast_template = templates_environment.get_template("fast_api__init__.jinja")
        fast_template_rendered = fast_template.render()
        with open("app/__init__.py", "w") as fast_api_init:
            fast_api_init.write(fast_template_rendered)

    @classmethod
    def run(cls) -> None:
        cls.generate_app()
        for folder, files in FOLDERS_FILES.items():
            os.mkdir(f"app/{folder}")
            for file in files:
                with open(f"app/{folder}/{file}.py", "w") as gen_file:
                    if file.startswith("__"):
                        template = templates_environment.get_template(
                            f"{folder + file}.jinja"
                        )
                    else:
                        template = templates_environment.get_template(f"{file}.jinja")
                    rendered_template = template.render()
                    gen_file.write(rendered_template)


if __name__ == "__main__":
    faag_cli = Faag()
    faag_cli.run()
