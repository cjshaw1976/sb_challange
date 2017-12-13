from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    id_number = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    address = models.TextField(max_length=100, blank=True)
    headshot_image = models.ImageField('profile picture',
                               upload_to='avatars/',
                               null=True, blank=True)
    residence_image = models.ImageField('profile picture',
                              upload_to='avatars/',
                              null=True, blank=True)
    signature_image = models.ImageField('profile picture',
                              upload_to='avatars/',
                              null=True, blank=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE,
                              related_name='customer')
    created_date = models.DateTimeField(default=datetime.now, blank=True)

# Todo, create folder for user id for Images
