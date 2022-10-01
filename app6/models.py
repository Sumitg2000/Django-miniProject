from django.db import models

# Create your models here.

class gymInfo(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Service = models.CharField(max_length=255)
    Msg = models.CharField(max_length=255)

    def __str__(self):
        return self.Name








