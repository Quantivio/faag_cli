import os

from faag_cli.constants import FOLDERS_FILES
from utils.templates_loader import templates_environment


def faag():
    for folder, files in FOLDERS_FILES.items():
        os.mkdir(folder)
        for file in files:
            with open(f"{folder}/{file}.py", "w") as gen_file:
                if file.startswith("__"):
                    template = templates_environment.get_template(
                        f"{folder + file}.jinja"
                    )
                else:
                    template = templates_environment.get_template(f"{file}.jinja")
                rendered_template = template.render()
                gen_file.write(rendered_template)


if __name__ == "__main__":
    faag()
