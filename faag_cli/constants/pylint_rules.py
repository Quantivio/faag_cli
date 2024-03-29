PYLINT_RULES = {
    "pylint": {
        "main": {
            "fail-under": 10.0,
            "ignore": ["CVS"],
            "ignore-patterns": ["^\\.#"],
            "jobs": 1,
            "limit-inference-results": 100,
            "persistent": True,
            "py-version": "3.11",
            "suggestion-mode": True,
        },
        "basic": {
            "argument-naming-style": "snake_case",
            "attr-naming-style": "snake_case",
            "bad-names": ["foo", "bar", "baz", "toto", "tutu", "tata"],
            "class-attribute-naming-style": "any",
            "class-const-naming-style": "UPPER_CASE",
            "class-naming-style": "PascalCase",
            "const-naming-style": "UPPER_CASE",
            "docstring-min-length": -1,
            "function-naming-style": "snake_case",
            "good-names": ["i", "j", "k", "ex", "Run", "_"],
            "inlinevar-naming-style": "any",
            "method-naming-style": "snake_case",
            "module-naming-style": "snake_case",
            "no-docstring-rgx": "^_",
            "property-classes": ["abc.abstractproperty"],
            "variable-naming-style": "snake_case",
        },
        "classes": {
            "defining-attr-methods": [
                "__init__",
                "__new__",
                "setUp",
                "__post_init__",
            ],
            "exclude-protected": [
                "_asdict",
                "_fields",
                "_replace",
                "_source",
                "_make",
            ],
            "valid-classmethod-first-arg": ["cls"],
            "valid-metaclass-classmethod-first-arg": ["cls"],
        },
        "design": {
            "max-args": 5,
            "max-attributes": 7,
            "max-bool-expr": 5,
            "max-branches": 12,
            "max-locals": 15,
            "max-parents": 7,
            "max-public-methods": 20,
            "max-returns": 6,
            "max-statements": 50,
        },
        "exceptions": {"overgeneral-exceptions": ["BaseException", "Exception"]},
        "format": {
            "ignore-long-lines": "^\\s*(# )?<?https?://\\S+>?$",
            "indent-after-paren": 4,
            "indent-string": "    ",
            "max-line-length": 120,
            "max-module-lines": 1000,
        },
        "imports": {"known-third-party": ["enchant"]},
        "logging": {"logging-format-style": "old", "logging-modules": ["logging"]},
        "messages control": {
            "confidence": [
                "HIGH",
                "CONTROL_FLOW",
                "INFERENCE",
                "INFERENCE_FAILURE",
                "UNDEFINED",
            ],
            "disable": [
                "raw-checker-failed",
                "bad-inline-option",
                "locally-disabled",
                "file-ignored",
                "suppressed-message",
                "useless-suppression",
                "deprecated-pragma",
                "use-symbolic-message-instead",
                "missing-class-docstring",
                "missing-function-docstring",
                "missing-module-docstring",
                "no-else-return",
                "duplicate-code",
                "no-member",
                "global-statement",
                "consider-using-enumerate",
            ],
            "enable": ["c-extension-no-member"],
        },
        "method_args": {
            "timeout-methods": [
                "requests.api.delete",
                "requests.api.get",
                "requests.api.head",
                "requests.api.options",
                "requests.api.patch",
                "requests.api.post",
                "requests.api.put",
                "requests.api.request",
            ]
        },
        "miscellaneous": {"notes": ["FIXME", "XXX", "TODO"]},
        "refactoring": {
            "max-nested-blocks": 5,
            "never-returning-functions": ["sys.exit", "argparse.parse_error"],
        },
        "reports": {
            "evaluation": "max(0, 0 if fatal else 10.0 - ((float(5 * error + warning + refactor + convention) / "
            "statement) * 10))",
            "score": True,
        },
        "similarities": {
            "ignore-comments": True,
            "ignore-docstrings": True,
            "ignore-imports": True,
            "ignore-signatures": True,
            "min-similarity-lines": 4,
        },
        "spelling": {
            "max-spelling-suggestions": 4,
            "spelling-ignore-comment-directives": "fmt: on,fmt: off,noqa:,noqa,nosec,isort:skip,mypy:",
        },
        "string": {},
        "typecheck": {
            "contextmanager-decorators": ["contextlib.contextmanager"],
            "ignore-none": True,
            "ignore-on-opaque-inference": True,
            "ignored-checks-for-mixins": [
                "no-member",
                "not-async-context-manager",
                "not-context-manager",
                "attribute-defined-outside-init",
            ],
            "ignored-classes": [
                "optparse.Values",
                "thread._local",
                "_thread._local",
                "argparse.Namespace",
            ],
            "missing-member-hint": True,
            "missing-member-hint-distance": 1,
            "missing-member-max-choices": 1,
            "mixin-class-rgx": ".*[Mm]ixin",
        },
        "variables": {
            "allow-global-unused-variables": True,
            "callbacks": ["cb_", "_cb"],
            "dummy-variables-rgx": "_+$|(_[a-zA-Z0-9_]*[a-zA-Z0-9]+?$)|dummy|^ignored_|^unused_",
            "ignored-argument-names": "_.*|^ignored_|^unused_",
            "redefining-builtins-modules": [
                "six.moves",
                "past.builtins",
                "future.builtins",
                "builtins",
                "io",
            ],
        },
    }
}
