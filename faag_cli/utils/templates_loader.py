from jinja2 import Environment, PackageLoader, select_autoescape

templates_environment = Environment(
    loader=PackageLoader("faag_cli", "templates"), autoescape=select_autoescape()
)
