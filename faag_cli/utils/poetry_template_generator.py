from box import Box

from faag_cli.constants.constants import FRAMEWORK_PACKAGES, POETRY_TEMPLATE


def generate_poetry_template(app_name: str, app_type: str) -> dict:
    """
    This method generates the poetry template for the project.
    :param app_name: The name of the app to be generated.
    :param app_type: The type of the app to be generated.
    :return: The poetry template.
    """
    poetry_template: Box = Box(POETRY_TEMPLATE)
    framework_packages: Box = Box(FRAMEWORK_PACKAGES)
    poetry_template.tool.poetry.name = app_name
    poetry_template.tool.poetry.description = f"{app_type} app generated using faag-cli"
    if app_type == "flask":
        poetry_template.tool.poetry.dependencies.update(framework_packages.flask)
    else:
        poetry_template.tool.poetry.dependencies.update(framework_packages.fast)
    return poetry_template.to_toml()
