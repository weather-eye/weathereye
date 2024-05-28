"""Main module."""
import os
import click
import ansible_runner


# path containing playbooks and settings files
playbooks_path = os.path.join(os.path.dirname(__file__), 'playbooks')
# path to SURFACE configuration webapp project folder
webapp_project_path = os.path.join(os.path.dirname(__file__), 'playbooks', 'project', 'wx_django',)


# retrieve and set SURFACE environment variables
def configure_surface(ansible_extravars):
    # configure web app playbook to django webapp folder path
    with open(ansible_extravars, 'a') as extravars_file:
            extravars_file.write(f'\ndjango_webapp_path: {webapp_project_path}')

    try:
        # start web app to configure SURFACE environment variables
        playbook_result = ansible_runner.run(private_data_dir=playbooks_path, 
                                             playbook='config_webapp.yml',)

        if playbook_result.status == "successful":
            pass
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
    

# execute SURFACE playbook
def install_surface():
    try:
        # install SURFACE
        playbook_result = ansible_runner.run(private_data_dir=playbooks_path, 
                                             playbook='install_surface.yml',)

        if playbook_result.status == "successful":
            click.echo(click.style("\nSURFACE successfully installed locally!", fg='green', bold=True))
        else:
            click.echo(click.style("\nAn error occured during SURFACE installation.", fg='red'))
            click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))

            return False

        return True

    except Exception as error:

        click.echo(click.style("An error occured during SURFACE installation.", fg='red'))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))
        click.echo(f"{error}", err=True)
        
        return False
    

# execute SURFACE playbook on remote machines
def remote_install_surface():
    try:
        # install SURFACE on a remote machine
        playbook_result = ansible_runner.run(private_data_dir=playbooks_path, 
                                             playbook='remote_install_surface.yml',)

        if playbook_result.status == "successful":
            click.echo(click.style("\nSURFACE successfully installed!", fg='green', bold=True))
        else:
            click.echo(click.style("\nAn error occured during SURFACE installation.", fg='red'))
            click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))

            return False

        return True

    except Exception as error:
       
        click.echo(click.style("\nAn error occured during SURFACE installation.", fg='red'))
        click.echo(click.style("see docs.weathereye.org for project documentation.", fg='red'))
        click.echo(f"{error}", err=True)
    
        return False