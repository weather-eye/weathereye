"""Console script for weathereye."""
import sys
import click
import logging

import weathereye.execute_playbooks as ex
from weathereye.utils import supported_os as so

logger = logging.getLogger(__name__)


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye install command group
@main.group()
def install():
    """WeatherEye install command"""
    pass


# command to install surface cdms
@install.command()
def surface():
    # Confirm SURFACE CDMS install with user
    if not click.confirm(click.style("This will install SURFACE CDMS and additional required dependencies. Proceed?", fg='yellow', bold=True)):
        return

    logger.info("Attempting to install SURFACE CDMS")

    # check if OS is supported before surface cdms install
    if so.check_sys():
        return

    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")

    # install SURFACE
    if not ex.run_surface_playbook():
        return


# command to install surface on a romote machine
@install.command()
def surface_remote():
    # Confirm remote SURFACE CDMS install with user
    if not click.confirm(click.style("This will install SURFACE CDMS and additional required dependencies on remote systems. Proceed?", fg='yellow', bold=True)):
        return
    
    logger.info("Attempting to install SURFACE CDMS on a remote machine")

    # check if OS is supported before surface cdms install
    ##########
    
    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")

    # install SURFACE
    if not ex.remote_run_surface_playbook():
        return
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
