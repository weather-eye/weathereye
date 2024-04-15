"""Console script for weathereye."""
import sys
import click


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye install command group
@main.group()
def install():
    """WeatherEye install command"""
    pass


# command to install surface
@install.command()
def surface():
    """Command to install SURFACE CDMS"""

    click.echo("Installing surface CDMS...")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
