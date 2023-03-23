"""
Description: This file contains the constants that will be used in the project.
"""
from box import Box

"""
FOLDERS_FILES is a dictionary that contains the folders and files that will be created.
Acts as a template for the project structure.
"""

FOLDERS_FILES = Box(
    {
        "config": [
            "__init__",
            "constants",
            "config",
        ],
        "connection": [
            "__init__",
        ],
        "controller": [
            "__init__",
            "sample_controller",
        ],
        "schemas": [
            "__init__",
        ],
        "request": [],
        "response": [
            "common_response_schema",
            "user_response_schema",
        ],
        "utils": [
            "__init__",
            "logger",
        ],
        "model": [
            "__init__",
            "sample_model",
        ],
        "service": [
            "__init__",
            "sample_service",
        ],
        "dao": [
            "__init__",
            "sample_dao",
        ],
    }
)

OTHER_FILES = Box(
    {
        "others": [
            ".gitignore",
            ".env",
        ]
    }
)

FRAMEWORK_PACKAGES = Box(
    {
        "fast": {
            "fastapi": "0.95.0",
            "uvicorn": "0.21.1",
        },
        "flask": {
            "flask": "2.2.3",
            "gunicorn": "20.1.0",
        },
    }
)

POETRY_TEMPLATE = Box(
    {
        "tool": {
            "poetry": {
                "name": "sample-app",
                "version": "0.1.0",
                "description": "",
                "authors": [],
                "readme": "README.md",
                "packages": [{"include": "sample_app"}],
                "dependencies": {
                    "python": "^3.11",
                    "pydantic": "^1.10.7",
                    "python-dotenv": "^1.0.0",
                },
                "group": {
                    "dev": {
                        "dependencies": {
                            "black": "23.1.0",
                            "pytest": "7.2.2",
                            "pytest-cov": "4.0.0",
                            "pre-commit": "^3.2.0",
                            "ruff": "^0.0.257",
                            "isort": "^5.12.0",
                            "mypy": "^1.1.1",
                        }
                    }
                },
            },
            "black": {
                "line-length": 120,
            },
            "isort": {
                "profile": "black",
            },
            "ruff": {
                "src": ["."],
                "target-version": "py311",
                "fix": True,
                "show-source": True,
                "line-length": 120,
                "select": [
                    "E",
                    "F",
                    "N801",
                    "N802",
                    "N803",
                    "N805",
                    "N806",
                ],
                "flake8-quotes": {
                    "inline-quotes": "double",
                    "multiline-quotes": "double",
                    "docstring-quotes": "double",
                },
                "flake8-tidy-imports": {
                    "ban-relative-imports": "all",
                },
                "flake8-type-checking": {
                    "strict": True,
                },
                "isort": {
                    "combine-as-imports": True,
                },
            },
            "mypy": {
                "strict": True,
            },
        },
        "build-system": {
            "requires": ["poetry-core"],
            "build-backend": "poetry.core.masonry.api",
        },
    }
)
