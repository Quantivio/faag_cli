RUFF_RULES = {
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
    }
}
