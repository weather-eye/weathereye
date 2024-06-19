from django.db import models

# Create your models here.
class InstallType(models.Model):
    type = models.CharField(max_length=10, choices=[('remote', 'Remote'), ('local', 'Local')])

    def __str__(self):
        return self.type

