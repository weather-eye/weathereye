from platform import system
from distro import id, version
import click
import logging

logger = logging.getLogger(__name__)


host_system = system().lower()
host_name = id().lower()
host_version = version().lower()

# check if OS is supported
def check_sys():
    logger.info("Checking if OS is supported.")

    # supported os
    if host_system == 'linux' and host_name == "ubuntu" and host_version == "22.04":
        logger.info("OS is supported")

        click.echo(click.style(f"{host_system, host_name, host_version} is compatible with surface CDMS", fg='blue', bold=True))

        return False

    # if OS is not supported
    logger.warning("OS is currently not supported.")
    
    click.echo(f"{('macOS' if host_name == 'darwin' else host_name), host_version} is not currently supported for SURFACE CDMS")
    click.echo(click.style("see docs.weathereye.org for supported operating systems", fg='red', bold=True))

    return True