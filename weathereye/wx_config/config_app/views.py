from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InstallTypeForm
from .models import InstallType

def index(request):
    if request.method == 'POST':
        form = InstallTypeForm(request.POST)
        if form.is_valid():
            InstallType.objects.all().delete()  # Clear previous data to avoid duplicates
            form.save()
            return redirect(reverse('configure_surface'))
        else:
            print("Form is invalid")
    else:
        form = InstallTypeForm()
    return render(request, 'config_app/index.html', {'form': form})