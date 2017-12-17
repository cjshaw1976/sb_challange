from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/customer_<user_name>/<filename>
    return 'customer_{0}/{1}'.format(instance.user_name, filename)

class Customer(models.Model):
    user_name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    id_number = models.CharField(max_length=16)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=16)
    email_address = models.EmailField()
    physical_address = models.TextField(max_length=128)
    headshot_image = models.FileField('Customer Photo',
                               upload_to=user_directory_path)
    residence_image = models.FileField('Proof of residence',
                              upload_to=user_directory_path)
    signature_image = models.FileField('Customer Signature',
                              upload_to=user_directory_path)
    created_by = models.ForeignKey(User, related_name='customers')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
