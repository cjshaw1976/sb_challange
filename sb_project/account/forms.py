from django import forms

from .models import Customer

class AccountForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'user_name',
            'first_name',
            'last_name',
            'id_number',
            'phone_number',
            'email_address',
            'physical_address',
            'headshot_image',
            'residence_image',
            'signature_image',
        )
