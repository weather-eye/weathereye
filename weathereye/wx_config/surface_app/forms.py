from django import forms
from config_app.models import InstallType

class SurfaceConfigurationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SurfaceConfigurationForm, self).__init__(*args, **kwargs)
        
        install_type = InstallType.objects.last()
        
        if install_type and install_type.type == 'remote':
            self.fields['host'] = forms.CharField(
                label="Remote Host for SURFACE install:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control',})
            )
            self.fields['surface_repo_path'] = forms.CharField(
                label="Path on remote machine to clone SURFACE repository:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control',})
            )
            self.fields['remote_connect_password'] = forms.CharField(
                label="Password to connect to the remote machine:", 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control',})
            )
            self.fields['remote_root_password'] = forms.CharField(
                label="Root password on the remote machine:", 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control',})
            )
        elif install_type and install_type.type == 'local':
            self.fields['local_root_password'] = forms.CharField(
                label="Sudo password:", 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control',})
            )
            self.fields['surface_repo_path'] = forms.CharField(
                label="Path to clone SURFACE repository:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control',})
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
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    admin = forms.CharField(
        label="Admin Username:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    admin_email = forms.CharField(
        label="Admin Email:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
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
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    lrgs_password = forms.CharField(
        label="LRGS Password:", 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control',})
    )
    timezone_name = forms.CharField(
        label="Timezone Name:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    timezone_offset = forms.CharField(
        label="Timezone Offset:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    map_latitude = forms.CharField(
        label="Map Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    map_longitude = forms.CharField(
        label="Map Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    map_zoom = forms.IntegerField(
        label="Map Zoom Level:", 
        required=True, 
        widget=forms.NumberInput(attrs={'id':'zoomField','class': 'form-control',})
    )
    spatial_analysis_initial_latitude = forms.CharField(
        label="Spatial Analysis Initial Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_initial_longitude = forms.CharField(
        label="Spatial Analysis Initial Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_final_latitude = forms.CharField(
        label="Spatial Analysis Final Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_final_longitude = forms.CharField(
        label="Spatial Analysis Final Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
