"""Console script for weathereye."""
import os
import sys
import click
import time

import weathereye.weathereye as wx


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye install command group
@main.command()
# prompt for sudo password
@click.option('--sudo-password', prompt=True, hide_input=True, required=True, confirmation_prompt=True, help='Sudo password to install SURFACE')
def install(sudo_password):
    """WeatherEye install / configuration command"""

    # path to pipx weathereye virtual environment
    venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 'bin', 'activate')

    # check if weathereye venv is activated
    venv_name = 'weathereye'

    if 'VIRTUAL_ENV' in os.environ:
        current_venv = os.path.basename(os.environ['VIRTUAL_ENV'])
        if current_venv == venv_name:
            click.echo(click.style(f"Virtual environment '{venv_name}' is activated.", fg='green'))
        else:
            click.echo(click.style(f"Warning: There is a problem with virtual environment: '{venv_name}'", fg='red'))
            click.echo(click.style("\nAttention, Run the following command before installing any packages with weathereye!", fg='yellow'))
            click.echo(click.style(f"source {venv_path}", fg='green'))
            return False
    else:
        click.echo(click.style(f"Warning: There is a problem with virtual environment: '{venv_name}'", fg='red'))
        click.echo(click.style("\nAttention, Run the following command before installing any packages with weathereye!", fg='yellow'))
        click.echo(click.style(f"source {venv_path}", fg='green'))
        return False
    
    wx.wx_configuration(sudo_password) # begin wx configuration
    
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
