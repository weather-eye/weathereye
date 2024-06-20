from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InstallTypeForm
from surface_app.models import InstallType


def index(request):
    if request.method == 'POST':
        form = InstallTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('configure_surface')) # Redirect to surfacae configuration site after saving
    else:
        form = InstallTypeForm()

    return render(request, 'config_app/index.html', {'form': form})
