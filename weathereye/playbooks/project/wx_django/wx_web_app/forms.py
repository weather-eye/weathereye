import os
from django import forms

class SurfaceConfigurationForm(forms.Form):
    # open install type file to determine which form items the user should see
    install_type_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'env', 'install_type')
    with open(install_type_path, 'r') as file:
        install_type = file.readline().strip()

    if install_type == "remote":
        host = forms.CharField(
            label="Remote Host for SURFACE install:", 
            required=True, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. username@xxx.xxx.xx.xxx',})
        )
        surface_repo_path = forms.CharField(
            label="Path on remote machine to clone SURFACE repository:", 
            required=True, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. /remote/machine/path/to/desktop/',})
        )
        remote_connect_password = forms.CharField(
            label="Password to connect to the remote machine:", 
            required=True, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. remotepassword',})
        )
        remote_root_password = forms.CharField(
            label="Root password on the remote machine:", 
            required=True, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. rootpassword',})
        )
    else:
        host = forms.CharField(
            label="Host for SURFACE install:", 
            required=False, 
            initial="localhost",
            widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'localhost'})
        )
        surface_repo_path = forms.CharField(
            label="Path to clone SURFACE repository:", 
            required=True, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. /path/to/desktop/',})
        )

    with_data = forms.ChoiceField(
        label="Start with Backup data:", 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        required=True, 
        initial='no',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input',})
    )
    data_path = forms.CharField(
        label="Backup data file path on host machine:", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. /path/to/backup/file',})
    )
    admin = forms.CharField(
        label="Admin Username:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. admin',})
    )
    admin_email = forms.CharField(
        label="Admin Email:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. admin@example.com',})
    )
    admin_password = forms.CharField(
        label="Admin Password:", 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control',})
    )
    
    # New form fields
    lrgs_user = forms.CharField(
        label="LRGS User:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. lrgs_user',})
    )
    lrgs_password = forms.CharField(
        label="LRGS Password:", 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control',})
    )
    timezone_name = forms.CharField(
        label="Timezone Name:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. America/New_York',})
    )
    timezone_offset = forms.CharField(
        label="Timezone Offset:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. -0500',})
    )
    map_latitude = forms.CharField(
        label="Map Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. 40.7128'})
    )
    map_longitude = forms.CharField(
        label="Map Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. -74.0060'})
    )
    map_zoom = forms.IntegerField(
        label="Map Zoom Level:", 
        required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. 10',})
    )
    spatial_analysis_initial_latitude = forms.CharField(
        label="Spatial Analysis Initial Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. 40.7128',})
    )
    spatial_analysis_initial_longitude = forms.CharField(
        label="Spatial Analysis Initial Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. -74.0060',})
    )
    spatial_analysis_final_latitude = forms.CharField(
        label="Spatial Analysis Final Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. 40.7128',})
    )
    spatial_analysis_final_longitude = forms.CharField(
        label="Spatial Analysis Final Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field', 'placeholder': 'e.g. -74.0060',})
    )
