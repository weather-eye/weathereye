from django.db import models

class InstallType(models.Model):
    INSTALL_CHOICES = [
        ('remote', 'Remote'),
        ('local', 'Local'),
    ]
    install_type = models.CharField(max_length=6, choices=INSTALL_CHOICES)

    def __str__(self):
        return self.install_type