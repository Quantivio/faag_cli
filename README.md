# Faag-CLI

**FastAPI/Flask project generator with the best folder structure.** (Fast/Flask Architecture App Generator)
Flask / FastAPI app generator with a maintainable architecture and sample codes for the best practices.
Currently, supports generation of FastAPI apps only. Flask support is coming soon. Currently, in `pre-release`. Feel
free
to raise suggestions and issues. This package is made with [Typer](https://typer.tiangolo.com/).

## Installation

```bash
poetry add faag-cli
```

```bash
pip install faag-cli
```

# Usage

Currently, we support generation of apps only. Adding support for other features like adding models, routes, etc. is
coming soon.

## To generate a FastAPI/Flask app

```faag generate``` will automatically generate a Fast App by default. You can also specify the type of app you want to
generate with the `--type` flag. Default app will be generated with 'sample_app' as the name. You can also specify the
name of the app with the `--name` flag.

```bash
 Usage: faag [OPTIONS] COMMAND [ARGS]...

 FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI. 

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v        Prints the version of Faag CLI                                                          │
│ --install-completion            Install completion for the current shell.                                               │
│ --show-completion               Show completion for the current shell, to copy it or customize the installation.        │
│ --help                          Show this message and exit.                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                         │
│ generate          FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

1. Help
    ```bash
    faag --help
    ```

2. Generate a FastAPI app
    ```bash
   faag generate
    ```

3. Generate a FastAPI/Flask App with custom app name
    ```bash
   faag generate --type fast --name fast_app
   faag generate -t flask -n flask_app
    ```

4. View options for generating a FastAPI/Flask app
    ```bash
   faag generate --help
    ```

# Setup for development

> ## Virtual environment setup with Poetry
> 1. Create a fork of the repository
> 2. Clone the repository to your local machine
     `git clone git@github.com:<username>/PyNotion.git`
> 3. Install poetry with `pip install poetry` or `pip3 install poetry`
> 4. Navigate to the root of the project and run `poetry install`

> ## Setup Pre-commit hooks
> 1. Install pre-commit hooks `pre-commit install`
> 2. Migrate pre-commit configs `pre-commit migrate-config`
> 3. In case of error run `git config --global --unset-all core.hooksPath` or `git config --unset-all core.hooksPath`

## Contribution Guidelines

Thank your for taking your valuable time to contribute to Faag-CLI.
Pull requests are welcome. For major changes, please open an issue
first to discuss what you would like to change.
