from django.db import models

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Friends(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Pages(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    names = models.CharField(max_length=20)
    images = models.ImageField(upload_to='images/', blank=True)
    date_addeds = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.names

    class Meta:
        ordering = ['-id']