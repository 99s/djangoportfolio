from django.db import models
from PIL import Image


# Create your models here.

# Use JS to upload fixed size image


class Job(models.Model):
    image = models.ImageField(upload_to='images/',
        null=True,
        blank=True,
        editable=True)
    summary = models.CharField(max_length=200)
    

    