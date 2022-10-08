from rich import print as rprint


def default_help_message() -> None:
    rprint(
        "\n[bold red]🚨Error: [green]No options specified.[/bold red]"
        "[red] Please specify an option to generate a new FastAPI/Flask project or add a new feature [ --generate | --feature ][/red]\n"
        "\nUse the --help option to see the available options\n",
        "\nUsage: faag_cli [OPTIONS] COMMAND [ARGS]...\n\nOptions:"
        "\n\t--help Shows list of commands and their usage"
        "\n\t--generate -gen Generate a new FastAPI/Flask project"
        "\n\t--feature -f Generate a new feature for the project [Coming soon...]",
    )
