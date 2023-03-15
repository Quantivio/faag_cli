"""
Description: Enum class for the different types of faag apps.
"""

from enum import Enum

# Two different options of faag app types. Can be used in typer prompt to show the user the options.


class AppTypes(Enum):
    FLASK = "flask"
    FAST = "fast"
