"""Main module."""
import os
import click
import ansible_runner


# path containing wx configuration playbook
wx_playbook_path = os.path.join(os.path.dirname(__file__), 'wx_playbook')

# path to sudo password
sudo_password_path = os.path.join(os.path.dirname(__file__), 'wx_playbook', 'env', 'become_password')

# retrieve and set SURFACE environment variables
def wx_configuration(sudo_password):
    try:
        # sudo password required for wx_configuratio playbook executeion
        with open(sudo_password_path, 'w') as sudo_password_file:
            sudo_password_file.write(sudo_password)

        # start web app to configure and install wx apps
        playbook_result = ansible_runner.run(private_data_dir=wx_playbook_path, 
                                             playbook='wx_configuration.yml',)

        if playbook_result.status == "successful":
            click.launch("http://localhost:52376/")
        else:
            click.echo(click.style("\nAn error occured while configuring SURFACE environment variables .", fg='red'))
            click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))

            return False

        return True

    except Exception as error:
        click.echo(click.style("An error occured during SURFACE installation.", fg='red'))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))
        click.echo(f"{error}", err=True)
        
        return False
    