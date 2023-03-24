from box import Box

from faag_cli.constants.constants import FRAMEWORK_PACKAGES, POETRY_TEMPLATE
from faag_cli.constants.pylint_rules import PYLINT_RULES
from faag_cli.constants.ruff_rules import RUFF_RULES


def generate_poetry_template(app_name: str, app_type: str, linter: str) -> str:
    """
    This method generates the poetry template for the project.
    :param app_name: The name of the app to be generated.
    :param app_type: The type of the app to be generated.
    :param linter: The linter to be used for the project.
    :return: The poetry template.
    """
    poetry_template: Box = Box(POETRY_TEMPLATE)
    framework_packages: Box = Box(FRAMEWORK_PACKAGES)
    poetry_template.tool.poetry.name = app_name
    poetry_template.tool.poetry.description = f"{app_type} app generated using faag-cli"
    if linter == "pylint":
        poetry_template.tool.update(PYLINT_RULES)
        poetry_template.tool.poetry.group.dev.dependencies.update(
            {
                "ruff": "^0.0.257",
            }
        )
    else:
        poetry_template.tool.update(RUFF_RULES)
        poetry_template.tool.poetry.group.dev.dependencies.update(
            {
                "pylint": "^2.17.1",
            }
        )
    if app_type == "flask":
        poetry_template.tool.poetry.dependencies.update(framework_packages.flask)
    else:
        poetry_template.tool.poetry.dependencies.update(framework_packages.fast)
    return poetry_template.to_toml()
