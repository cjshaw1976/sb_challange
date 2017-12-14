from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/customer_<id>/<filename>
    return 'customer_{0}/{1}'.format(instance.customer.id, filename)

class Customer(models.Model):
    user_name = models.CharField(max_length=16)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    id_number = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=16)
    email_address = models.EmailField()
    physical_address = models.TextField(max_length=128, blank=True)
    headshot_image = models.ImageField('Customer Photo',
                               upload_to=user_directory_path,
                               null=True, blank=True)
    residence_image = models.ImageField('Proof of residence',
                              upload_to=user_directory_path,
                              null=True, blank=True)
    signature_image = models.ImageField('Customer Signature',
                              upload_to=user_directory_path,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='customers')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
