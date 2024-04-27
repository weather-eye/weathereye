import os
import logging
import click
import ansible_runner
import getpass
import subprocess

logger = logging.getLogger(__name__)

# playbooks folder path
playbooks_path = os.path.dirname(__file__) + "/playbooks"

# docker playbook path
docker_playbook_path = os.path.dirname(__file__) + "/playbooks/install_docker.yml"


# execute docker playbook
def run_docker_playbook():
    logging.warning("Attempting to execute docker playbook...")

    try:
        # prompt user for sudo password then run playbook
        ans_run = ansible_runner.run(playbook=docker_playbook_path,
                                     extravars={"user":getpass.getuser(),
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
    

# execute docker playbook on remote machines
def remote_run_docker_playbook():
    logging.warning("Attempting to execute docker playbook...")

    try:
        # inventory path
        inventory_path = os.path.dirname(__file__) + "/playbooks/inventory"

        # custom ansible config path
        custom_config_path = os.path.dirname(__file__) + "/playbooks/ansible_custom.cfg"

        # appending inventory path to custom ansible config file
        custom_config = open(custom_config_path, "a")
        custom_config.write(f"inventory = {inventory_path}")
        custom_config.close()

        # prompt user for sudo password then run playbook
        ans_run = ansible_runner.run(playbook=docker_playbook_path,
                                     extravars={"user":getpass.getuser(),
                                                "sudo_password":getpass.getpass(f"[sudo] password for {getpass.getuser()}: "),
                                                },
                                     private_data_dir=playbooks_path)

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