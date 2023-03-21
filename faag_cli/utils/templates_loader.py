"""
Description: Loads all Jinja templates from the templates directory
"""

from jinja2 import Environment, PackageLoader, select_autoescape

templates_environment = Environment(loader=PackageLoader("faag_cli", "templates"), autoescape=select_autoescape())
