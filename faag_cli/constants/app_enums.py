"""
Description: Enum class for the different types of faag_cli apps.
"""

from enum import Enum

# Two different options of faag_cli app types. Can be used in typer prompt to show the user the options.


class AppTypes(Enum):
    FLASK = "flask"
    FAST = "fast"


class LinterTypes(Enum):
    FLAKE8 = "flake8"
    PYLINT = "pylint"
    RUFF = "ruff"


class FormatterTypes(Enum):
    BLACK = "black"
    AUTOPEP8 = "autopep8"
