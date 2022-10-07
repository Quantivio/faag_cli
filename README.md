# Faag-CLI

**FastAPI/Flask project generator with the best folder structure.** (Fast/Flask Architecture App Generator)
Flask / FastAPI app generator with a maintainable architecture and sample codes for the best practices.
Currently supports generation of FastAPI apps only. Flask support is coming soon. Currently in `pre-release`. Feel free
to raise suggesstions and issues. This package is made with [Typer](https://typer.tiangolo.com/).

## Installation

```bash
poetry add faag-cli
```

```bash
pip install faag-cli
```


# Usage

```bash
Usage: faag [OPTIONS]

 Generate a new FastAPI/Flask project
 
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --app                 -a       TEXT  Type of that should be generated. Default type is fast_api. Valid Options are: [fast_api, flask] [default: fast_api        |
│ --app-name            -an      TEXT  Name of the app [default: sampel_app]                                                                                      |
│ --install-completion                 Install completion for the current shell.                                                                                  |
│ --show-completion                    Show completion for the current shell, to copy it or customize the installation.                                           |
│ --help                               Show this message and exit.                                                                                                |
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

1. Help
    ```bash
    faag --help
    ```

2. Generate a FastAPI app
    ```bash
   faag
    ```

3. Generate a Fast APP with custom app name
    ```bash
   faag --app-name myapp
   faag -an myapp
    ```
   