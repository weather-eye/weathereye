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

    # install docker
    if not ex.run_docker_playbook():
        return 

    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")


# command to install surface on a romote machine
@install.command()
def remote_surface():
    # Confirm remote SURFACE CDMS install with user
    if not click.confirm(click.style("This will install SURFACE CDMS and additional required dependencies on remote systems. Proceed?", fg='yellow', bold=True)):
        return
    
    logger.info("Attempting to install SURFACE CDMS on a remote machine")

    # check if OS is supported before surface cdms install
    ##########

    # install docker
    if not ex.remote_run_docker_playbook():
        return 
    
    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
