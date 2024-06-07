"""Console script for weathereye."""
import os
import sys
import click

import weathereye.weathereye as ex


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye venv
@main.command()
def venv():
    """WeatherEye venv command, run this command before installing anything with weathereye."""
    # path to pipx weathereye virtual environment
    venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 'bin', 'activate')
    
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
    # path to sudo password
    sudo_password_file_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'become_password')

    # path to remote machine connection password
    #remote_connection_password_file_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'connection_password')

    # path to ansible extarvars
    ansible_extravars = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'extravars',)

    # path to SURFACE installation type
    install_type = os.path.join(os.path.dirname(__file__), 'playbooks', 'env', 'install_type',)

    # clear variable file before install
    with open(ansible_extravars, 'w') as ef:
        ef.write('---')

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
    
    # click.launch("http://0.0.0.0:52376")
    click.echo(click.style("\nConfigure SURFACE at http://0.0.0.0:52376", fg='green'))
    click.confirm(click.style("\nSURFACE environment variables configuration complete?", fg='yellow'), abort=True)

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
