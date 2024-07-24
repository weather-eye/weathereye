import os


# path to ansible project folder
django_app_dir = os.path.dirname(os.path.dirname(__file__))

# path to ansible project folder
project_dir = os.path.join(django_app_dir, 'ansible', 'surface_app',)

# path to remote connection file
connection_password_file_path = os.path.join(project_dir, 'env', 'connection_password')

# path to root user password file
sudo_password_file_path = os.path.join(project_dir, 'env', 'become_password')

# path to sudo password used for local installs
local_sudo_password_path = os.path.join(os.path.dirname(django_app_dir ),'wx_playbook', 'env', 'become_password')

# path to surface variables file
variable_file_path = os.path.join(project_dir, 'env', 'extravars',)

# path to production.env file
prod_env_file_path = os.path.join(project_dir, 'env', 'production.env',)

# path to remote hosts path
hosts_file_path = os.path.join(project_dir, 'inventory', 'hosts')


def replace_text_in_file(file_path, search_text, replace_text):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Replace the search text with the replacement text
        new_content = file_content.replace(search_text, replace_text)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
    except:
        pass


def write_out_surface_variables(form):
    # write out surface variables
    with open(variable_file_path, 'w') as vf:
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
        vf.write(f'"prod_env_path": "{prod_env_file_path}"\n')


def write_out_production_variables(form):
    # clear production.env of any previously entered settings
    with open(prod_env_file_path, 'r') as file:
        prod_lines = file.readlines()

    prod_index = None
    for index, line in enumerate(prod_lines):
        if line.strip() == '# USER MODIFIED SETTINGS':
            prod_index = index
            break

    if prod_index is not None:
        # Keep everything before the "# USER MODIFIED SETTINGS" section
        prod_new_lines = prod_lines[:prod_index + 1]

        # Write the modified contents back to the file
        with open(prod_env_file_path, 'w') as file:
            file.writelines(prod_new_lines)

    # Write out production.env variables
    with open(prod_env_file_path, 'a') as prod:
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


def write_out_host_connection_details(form, install_type):
    # write out remote host connection details 
    if install_type.install_type == 'remote':
        
        # Read the contents of the hosts file
        with open(hosts_file_path, 'r') as file:
            lines = file.readlines()

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
            with open(hosts_file_path, 'w') as file:
                file.writelines(new_lines)

        # write out remote connection password to the connection password file
        with open(connection_password_file_path, 'w') as connection_password_file:
            connection_password_file.write(form.cleaned_data["remote_connect_password"])

        # write root password to the sudo password file
        with open(sudo_password_file_path, 'w') as sudo_password_file:
            sudo_password_file.write(form.cleaned_data["root_password"])

    else:

        # on local installs write out a misc value to the connection password file
        with open(connection_password_file_path, 'w') as connection_password_file:
            connection_password_file.write('connection_password')

        # write root password to the sudo password file
        with open(sudo_password_file_path, 'w') as sudo_password_file:
            # path to where local sudo password is stored
            with open(local_sudo_password_path, 'r') as local_sudo_password:
                # write sudo password out
                sudo_password_file.write(local_sudo_password.read())


def process_form(form, install_type):

    # issue: changing root privileges for play
    # read username from file
    # with open(os.path.join(project_dir, 'env', 'user'), 'r') as file_object:
    #   # Read the entire file content into a string
    #   username = file_object.read().strip()

    # if install_type.install_type == "remote":
    #     # modify ansible cfg file with the root username
    #     replace_text_in_file(os.path.join(project_dir, 'project', 'ansible.cfg'), f'become_user={username}', 'become_user=root')
    # else:
    #     # modify ansible cfg file with the current username
    #     replace_text_in_file(os.path.join(project_dir, 'project', 'ansible.cfg'), 'become_user=root', f'become_user={username}')

    write_out_host_connection_details(form, install_type)

    write_out_surface_variables(form)

    write_out_production_variables(form)

    # set the required playbook file
    if install_type.install_type == 'remote':
        playbook_name = 'remote_install_surface.yml' # for remote installations
    else:
        playbook_name = 'install_surface.yml' # for local installations

    return project_dir, playbook_name