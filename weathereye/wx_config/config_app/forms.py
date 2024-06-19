from django import forms
from .models import InstallType

class InstallTypeForm(forms.ModelForm):
    class Meta:
        model = InstallType
        fields = ['type']
        widgets = {
            'type': forms.RadioSelect(choices=[('remote', 'Remote'), ('local', 'Local')])
        }
