from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
import pytz

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
    created_date = models.DateTimeField(default=timezone.now, blank=True)


class CustomerSession(models.Model):
    customer = models.OneToOneField(Customer)
    session = models.ForeignKey(Session)
    start_time = models.DateTimeField(default=timezone.now, blank=True)
    ip = models.GenericIPAddressField()
    agent = models.TextField(max_length=512)


class AccessLog(models.Model):
    SUCCESS = 'SUCCESS' # Greeen
    INFO = 'INFO'       # Blue
    WARN = 'WARN'       # Orange
    ERROR = 'ERROR'     # Red

    LEVEL_CHOICES = (
        (SUCCESS, 'success'),
        (INFO, 'info'),
        (WARN, 'warn'),
        (ERROR, 'error'),
    )
    
    timestamp = models.DateTimeField(default=timezone.now, blank=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default=SUCCESS)
    user = models.ForeignKey(User, related_name='accesslog', blank=True)
    customer = models.ForeignKey(Customer, related_name='accesslog', blank=True)
    notes  = models.TextField(max_length=256)
