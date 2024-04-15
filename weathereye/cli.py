"""Console script for weathereye."""
import sys
from platform import system
from distro import id, version
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

    # check if OS is supported before install
    host_system = system().lower()
    host_name = id()
    host_version = version()

    if host_system != 'linux':
        
        click.echo(f"{("macOS" if host_name == "darwin" else host_name), host_version} is not supported for surface CDMS")
        click.echo(click.style("see docs.weathereye.org for supported operating systems", fg='red', bold=True))

        return

    # begin surface cdms installation
    click.echo("Installing surface CDMS...")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover