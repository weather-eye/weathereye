import os
import logging
import click
import ansible_runner
import getpass
import subprocess

logger = logging.getLogger(__name__)


# execute docker playbook
def run_docker_playbook():
    logging.warning("Attempting to execute docker playbook...")

    try:
        playbook_path = os.path.dirname(__file__) + "/playbooks/install_docker.yml" # install_docker playbook path

        # prompt user for sudo password then run playbook
        ans_run = ansible_runner.run(playbook=playbook_path, extravars={
            "user":getpass.getuser(),
            "sudo_password":getpass.getpass(f"[sudo] password for {getpass.getuser()}: "),
            })

        logging.info(f"docker install {ans_run.status}")

        # throwing an exception if docker install was not successful
        if ans_run.status != "successful":
            raise Exception("Docker install failed.")

        return True

    except Exception as error:
        logging.error(f"docker playbook install failed...{error}")

        click.echo(click.style("An error occured during docker playbook installation.", fg='yellow', bold=True))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red', bold=True))
        
        return False