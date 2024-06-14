"""Console script for weathereye."""
import os
import sys
import click
import time

import weathereye.weathereye as ex


# path to pipx weathereye virtual environment
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 'bin', 'activate')


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye venv
@main.command()
def venv():
    """WeatherEye venv command, run this command before installing anything with weathereye."""
    
    click.echo(click.style("\nAttention, Run the following command before installing any packages with weathereye!", fg='yellow'))
    click.echo(click.style(f"source {venv_path}", fg='yellow'))


# WeatherEye install command group
@main.group()
def install():
    """WeatherEye install command"""
    pass


# command to install surface cdms
@install.command()
@click.option('--sudo-password', prompt=True, hide_input=True, required=True, confirmation_prompt=True, help='Sudo password to install SURFACE')
@click.option("--remote", "-r", is_flag=True, help="Install SURFACE on a remote machine")

def surface(remote, sudo_password):
    # check if weathereye venv is activated
    venv_name = 'weathereye'

    if 'VIRTUAL_ENV' in os.environ:
        current_venv = os.path.basename(os.environ['VIRTUAL_ENV'])
        if current_venv == venv_name:
            click.echo(f"Virtual environment '{venv_name}' is activated.", fg='green')
        else:
            click.echo(f"Warning: Virtual environment '{venv_name}' is not activated. Current active venv is '{current_venv}'.", fg='red')
            click.echo(click.style("\nAttention, Run the following command before installing any packages with weathereye!", fg='yellow'))
            click.echo(click.style(f"source {venv_path}", fg='yellow'))
            return False
    else:
        click.echo(f"Warning: Virtual environment '{venv_name}' is not activated. Current active venv is '{current_venv}'.", fg='red')
        click.echo(click.style("\nAttention, Run the following command before installing any packages with weathereye!", fg='yellow'))
        click.echo(click.style(f"source {venv_path}", fg='yellow'))
        return False
    
    # path to sudo password
    sudo_password_file_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'become_password')

    # path to remote machine connection password
    #remote_connection_password_file_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'connection_password')

    # path to ansible extarvars
    ansible_extravars = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'extravars',)

    # path to SURFACE installation type
    install_type = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'install_type',)

    # path to SURFACE config status
    config_status_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'config_status',)
    config_status = "incomplete"

    # progress file path
    progress_file_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'project', 'wx_django', 'static', 'misc', 'progress')

    # clear progress file before install
    with open(progress_file_path, 'w') as pf:
        pf.write('')

    # clear variable file before install
    with open(ansible_extravars, 'w') as ef:
        ef.write('---')

    # set config status to incomplete before install
    with open(config_status_path, 'w') as cs:
        cs.write(config_status)

    # write sudo password to file
    with open(sudo_password_file_path, 'w') as sudo_password_file:
        sudo_password_file.write(sudo_password)

    # write out install type to file
    if remote:
        with open(install_type, 'w') as it:
            it.write('remote')
    else:
        with open(install_type, 'w') as it:
            it.write('local')

    # start web app to configure SURFACE environment variables
    if not ex.configure_surface(ansible_extravars):
        return
    
    # click.launch("http://localhost:52376/")
    click.echo(click.style("\nConfigure SURFACE at http://localhost:52376/", fg='green'))
    # click.confirm(click.style("\nSURFACE environment variables configuration complete?", fg='yellow'), abort=True)
    
    # waiting for config status to return complete
    while (True):
        with open(config_status_path, 'r') as rcs:
            config_status = rcs.readline().strip()

        if config_status == "complete":
            break

        # wait 60 seconds before 
        time.sleep(60)


    # start SURFACE install
    click.echo("\nInstalling SURFACE CDMS...")

    # install SURFACE on a remote machine
    if remote:
        '''
        click.echo(click.style("\n\n\n[Remote host authentication details]", fg='blue', bold=True))

        # remote host connection password
        remote_connection_password = click.prompt('Please enter the SSH password for the REMOTE host', hide_input=True, confirmation_prompt=True)
        # write remote connection password to file
        with open(remote_connection_password_file_path, 'w') as remote_connection_password_file:
            remote_connection_password_file.write(remote_connection_password)

        # remote host sudo password
        remote_sudo_password = click.prompt('\nPlease enter the REMOTE HOST\'s sudo password', hide_input=True, confirmation_prompt=True)
        # write remote connection sudo password to file
        with open(sudo_password_file_path, 'w') as sudo_password_file:
            sudo_password_file.write(remote_sudo_password)
        '''

        if not ex.remote_install_surface():
            return
    
    # install SURFACE on host machine
    else:
        if not ex.install_surface():
            return
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
