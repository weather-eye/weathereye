import os
import pwd

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings
from .forms import SurfaceConfigurationForm
from .models import InstallType, AnsibleRun
from .tasks import install_surface, get_ansible_task_status
from .utils import process_form

# project directory and playbook name variables
project_dir = "" 
playbook_name = ""

# surface configuration view
def configure_surface(request):
    # Fetch the latest AnsibleRun and its status
    latest_ansible_run = AnsibleRun.objects.last()
    latest_status = latest_ansible_run.status if latest_ansible_run else None

    # Check if the status is valid and if any InstallType exists
    if not latest_status:
        install_type = InstallType.objects.last() # get installation type (remote or local)
    else:
        return redirect(reverse('wx_configuration')) # redirecting to the home page

    if request.method == 'POST':
        form = SurfaceConfigurationForm(request.POST)
        # Process the form data
        if form.is_valid():

            # process configuration data
            global project_dir, playbook_name 
            
            project_dir, playbook_name = process_form(form, install_type)
            
            task = install_surface.apply_async(args=[project_dir, playbook_name, install_type.install_type])

            url = reverse('config-complete', kwargs={'task_id': task.id})

            return redirect(url) # Redirect to config_complete page

    else:
        form = SurfaceConfigurationForm() # form

        # Get the current user's username
        username = os.getlogin()
        # Retrieve the home directory for the current user
        home_directory = pwd.getpwnam(username).pw_dir

        # users home directory to preload into surface_repo_path
        user_home_dir = home_directory

    return render(request, 'surface_app/configuration.html', {'form': form, 'user_home_dir': user_home_dir, 'install_type':  install_type.install_type, })


# get the status of the current task
@require_GET
def task_status(request, task_id):
    task_status = get_ansible_task_status(task_id)

    return JsonResponse(task_status)


# config_complete page view
def config_complete(request, task_id):
    # check if task id exists if not redirect to the home page (wx_configuration)
    if InstallType.objects.exists():
        return render(request, 'surface_app/config_complete.html', {'task_id': task_id})
    else:
        return redirect(reverse('wx_configuration'))
    

# # retry configuration with the same env variables
# def retry_config(request):
#     task = install_surface.apply_async(args=[project_dir, playbook_name])

#     url = reverse('config-complete', kwargs={'task_id': task.id})

#     return redirect(url) # Redirect to config_complete page