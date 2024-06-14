import os
import signal
import threading

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import SurfaceConfigurationForm

def configure_surface(request):
    if request.method == 'POST':
        form = SurfaceConfigurationForm(request.POST)
        if form.is_valid():
            # Process the form data
            # open install type file to determine which form items the user should see
            install_type_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'install_type')
            with open(install_type_path, 'r') as file:
                install_type = file.readline().strip()

            # path to remote connection file
            remote_connection_password_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'connection_password')

            # path to root user password file
            sudo_password_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'become_password')

            # path to surface variables file
            variable_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'extravars',)

            # path to production.env file
            prod_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'production.env',)
            
            # write out remote host
            # path to remote hosts path
            remote_hosts_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'inventory', 'hosts')

            # Read the contents of the hosts file
            with open(remote_hosts_file, 'r') as file:
                lines = file.readlines()

            # Read the contents of the production.env
            with open(prod_env_path, 'r') as file:
                prod_lines = file.readlines()

            # Find the index of the "# USER MODIFIED SETTINGS" section
            prod_index = None
            for index, line in enumerate(prod_lines):
                if line.strip() == '# USER MODIFIED SETTINGS':
                    prod_index = index
                    break

            # If the "# USER MODIFIED SETTINGS" section is found, modify the content
            if prod_index is not None:
                # Keep everything before the "# USER MODIFIED SETTINGS" section
                prod_new_lines = prod_lines[:prod_index + 1]

                # Write the modified contents back to the file
                with open(prod_env_path, 'w') as file:
                    file.writelines(prod_new_lines)

            # write out remote host connection details 
            if install_type == "remote":
                # Find the index of the [remote] section
                remote_index = None
                for index, line in enumerate(lines):
                    if line.strip() == '[remote]':
                        remote_index = index
                        break

                # If the [remote] section is found, modify the content
                if remote_index is not None:
                    # Keep everything before the [remote] section and add the new content
                    new_lines = lines[:remote_index + 1]
                    new_lines.append(f'\n{form.cleaned_data["host"].strip()}')

                    # Write the modified contents back to the file
                    with open(remote_hosts_file, 'w') as file:
                        file.writelines(new_lines)

                with open(remote_connection_password_file_path, 'w') as remote_connection_password_file:
                    remote_connection_password_file.write(form.cleaned_data["remote_connect_password"])
                
                with open(sudo_password_file_path, 'w') as sudo_password_file:
                    sudo_password_file.write(form.cleaned_data["remote_root_password"])

            # write out surface variables
            with open(variable_file, 'w') as vf:
                vf.write('---\n')
                # write surface_repo_path
                surface_repo_path = form.cleaned_data['surface_repo_path'].strip()
                if surface_repo_path[-1] == "/":
                    vf.write(f'"surface_repo_path": "{surface_repo_path}surface/"\n')
                else:
                    vf.write(f'"surface_repo_path": "{surface_repo_path}/surface/"\n')
                # write with_data
                vf.write(f'"with_data": "{form.cleaned_data["with_data"]}"\n')
                # write data file path
                vf.write(f'"data_path": "{form.cleaned_data["data_path"]}"\n')
                # write data filename
                vf.write(f'"data_file_name": "{form.cleaned_data["data_path"].strip("/").split("/")[-1]}"\n')
                # write admin
                vf.write(f'"admin": "{form.cleaned_data["admin"].strip()}"\n')
                # write admin_email
                vf.write(f'"admin_email": "{form.cleaned_data["admin_email"].strip()}"\n')
                # write admin_password
                vf.write(f'"admin_password": "{form.cleaned_data["admin_password"]}"\n')
                # path to production.env file
                vf.write(f'"prod_env_path": "{prod_env_path}"\n')

            # Write out production.env variables
            with open(prod_env_path, 'a') as prod:
                prod.write('\n\n')
                prod.write(f'LRGS_USER={form.cleaned_data["lrgs_user"].strip()}\n')
                prod.write(f'LRGS_PASSWORD={form.cleaned_data["lrgs_password"]}\n')
                
                prod.write('\n')
                prod.write(f'TIMEZONE_NAME={form.cleaned_data["timezone_name"].strip()}\n')
                prod.write(f'TIMEZONE_OFFSET={form.cleaned_data["timezone_offset"]}\n')

                prod.write('\n')
                prod.write(f'MAP_LATITUDE={form.cleaned_data["map_latitude"]}\n')
                prod.write(f'MAP_LONGITUDE={form.cleaned_data["map_longitude"]}\n')
                prod.write(f'MAP_ZOOM={form.cleaned_data["map_zoom"]}\n')

                prod.write('\n')
                prod.write(f'SPATIAL_ANALYSIS_INITIAL_LATITUDE={form.cleaned_data["spatial_analysis_initial_latitude"]}\n')
                prod.write(f'SPATIAL_ANALYSIS_INITIAL_LONGITUDE={form.cleaned_data["spatial_analysis_initial_longitude"]}\n')
                prod.write(f'SPATIAL_ANALYSIS_FINAL_LATITUDE={form.cleaned_data["spatial_analysis_final_latitude"]}\n')
                prod.write(f'SPATIAL_ANALYSIS_FINAL_LONGITUDE={form.cleaned_data["spatial_analysis_final_longitude"]}\n')

            # open config_status file and update it to complete
            config_status_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'config_status')
            with open(config_status_path, 'w') as cs:
                cs.write('complete')

            # redirect to success page
            return render(request, 'wx_web_app/success.html')  # Redirect to success page
    else:
        form = SurfaceConfigurationForm() # form
        user_home_dir = os.path.expanduser('~') # users home directory to preload into surface_repo_path
    return render(request, 'wx_web_app/configuration.html', {'form': form, 'user_home_dir': user_home_dir,})

def shutdown(request):

    return render(request, 'wx_web_app/shutdown.html')

def shutdown_server(request):
    # Send termination signal to the current process
    os.kill(os.getpid(), signal.SIGINT)

    return HttpResponse('Server shutting down...')

def get_install_progress(request):
    progress_file_path = os.path.join(settings.STATIC_DIR, 'misc', 'progress')

    try:
        with open(progress_file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    except Exception as e:
        return HttpResponse(str(e), status=500)

def simulate_progress(request):
    with open(os.path.join(settings.STATIC_DIR, 'misc', 'progress'), 'a') as file:
        file.write('p')
    return HttpResponse('File updated successfully')