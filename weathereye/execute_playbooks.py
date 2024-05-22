import os
import click
import subprocess

# getting path to the weathereye virtual environment activate script
venv_activate_script = os.path.dirname(__file__) # current script's directory
levels_up = 4 # number of directory levels to go up
for _ in range(levels_up):
    venv_activate_script = os.path.dirname(venv_activate_script)

# path to activate script for weathereye venv
venv_activate_script += "/bin/activate"

# path to Ansible config file
ansible_config_path = os.path.dirname(__file__) + "/playbooks/ansible.cfg"

# path to Ansible config file for localhost
localhost_ansible_config_path = os.path.dirname(__file__) + "/playbooks/ansible-localhost.cfg"

# surface playbook path
surface_playbook_path = os.path.dirname(__file__) + "/playbooks/install_surface.yml"

# surface remote playbook path
surface_remote_playbook_path = os.path.dirname(__file__) + "/playbooks/install_surface_remote.yml"


# execute surface playbook
def run_surface_playbook():
    try:
        # build the command to run SURFACE playbook
        ansible_command = [
            f"ANSIBLE_CONFIG={localhost_ansible_config_path}",
            "ansible-playbook",
            surface_playbook_path,
        ]

        # run the combined command as a subprocess
        subprocess.run(' '.join(ansible_command), shell=True)

        return True

    except Exception as error:

        click.echo(click.style("An error occured during SURFACE playbook installation.", fg='yellow', bold=True))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='yellow', bold=True))
        click.echo(click.style(f"{error}", fg='red'))
        
        return False
    

# execute surface playbook on remote machines
def remote_run_surface_playbook(hosts_list):
    try:
        # build the command to activate the venv and run SURFACE playbook
        ansible_command = [
            f"ANSIBLE_CONFIG={ansible_config_path}",
            f"ANSIBLE_INVENTORY={hosts_list}",
            "ansible-playbook",
            surface_remote_playbook_path,
        ]

        # # combine activation and Ansible command into a single command
        # activate_and_run_command = f"source {venv_activate_script} && {' '.join(ansible_command)}"

        # # run the combined command as a subprocess
        # subprocess.run(activate_and_run_command, shell=True)

        # run the combined command as a subprocess
        subprocess.run(' '.join(ansible_command), shell=True)

        return True

    except Exception as error:
       
        click.echo(click.style("An error occured during SURFACE playbook installation.", fg='yellow', bold=True))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='yellow', bold=True))
        click.echo(click.style(f"{error}", fg='red'))
        
        return False