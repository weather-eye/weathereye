import os
import logging
import click
import subprocess

logger = logging.getLogger(__name__)

# getting path to the weathereye virtual environment activate script
venv_activate_script = os.path.dirname(__file__) # current script's directory
levels_up = 4 # number of directory levels to go up
for _ in range(levels_up):
    venv_activate_script = os.path.dirname(venv_activate_script)

# path to activate script for weathereye venv
venv_activate_script += "/bin/activate"

# path to Ansible config file
ansible_config_path = os.path.dirname(__file__) + "/playbooks/ansible.cfg"

# path to Ansible config file
localhost_ansible_config_path = os.path.dirname(__file__) + "/playbooks/ansible-localhost.cfg"

# docker playbook path
docker_playbook_path = os.path.dirname(__file__) + "/playbooks/install_docker.yml"


# execute docker playbook
def run_docker_playbook():
    logging.warning("Attempting to execute docker playbook...")

    try:
        # build the command to activate the venv and run Docker playbook
        ansible_command = [
            f"ANSIBLE_CONFIG={localhost_ansible_config_path}",
            "ansible-playbook",
            docker_playbook_path,
        ]

        # run the combined command as a subprocess
        subprocess.run(' '.join(ansible_command), shell=True)

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
        # build the command to activate the venv and run Docker playbook
        ansible_command = [
            f"ANSIBLE_CONFIG={ansible_config_path}",
            "ansible-playbook",
            docker_playbook_path,
        ]

        # # combine activation and Ansible command into a single command
        # activate_and_run_command = f"source {venv_activate_script} && {' '.join(ansible_command)}"

        # # run the combined command as a subprocess
        # subprocess.run(activate_and_run_command, shell=True)
        
        # run the combined command as a subprocess
        subprocess.run(' '.join(ansible_command), shell=True)

        return True

    except Exception as error:
        logging.error(f"docker playbook install failed...{error}")

        click.echo(click.style("An error occured during docker playbook installation.", fg='yellow', bold=True))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red', bold=True))
        
        return False