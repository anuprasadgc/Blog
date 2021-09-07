from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)