from django.urls import path
from surface_app import views

urlpatterns = [
    path('', views.configure_surface, name='configure_surface'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('shutdown-server/', views.shutdown_server, name='shutdown_server'),
    # path('install-progress/', views.get_install_progress, name='get_install_progress'),
    # path('installation-progress/', views.simulate_progress, name='simulate_progress'),
]