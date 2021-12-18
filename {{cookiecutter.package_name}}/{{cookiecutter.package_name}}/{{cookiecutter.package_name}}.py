import sys
import click

@click.group()
def main() -> None:
	pass

@click.command()
def cli_test() -> None:
	"""
	Function used to test click CLI
	"""

	print("Click CLI is working!")

	return


main.add_command(cli_test, name="cli-test")

if __name__ == "__main__":
	sys.exit(main())
