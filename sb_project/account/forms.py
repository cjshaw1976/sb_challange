from django import forms

from django.core.exceptions import ValidationError
# from django.utils.image import Image

from .models import Customer

import re


class AccountForm(forms.ModelForm):
    def clean_id_number(self):
        # Check id number is valid format
        # 2 digits, optional space or minus, 6 or 7 digits, one letter, 2 digits
        data = self.cleaned_data['id_number']

        if not re.match("^(?:\d{2}(?:\s|\-)\d{6,7}[a-zA-Z]\d{2})|(?:\d{8,9}[a-zA-Z]\d{2})$", data):
            # Does not match
            raise ValidationError('Invalid ID Format')

        # Remember to always return the cleaned data.
        return data

    def clean_headshot_image(self):
        # Check that images are included and in jpg format
        data = self.cleaned_data.get(['headshot_image'])

        if data:
            return data
#            format = Image.open(data.file).format
#            data.file.seek(0)
#            if format in ['jpeg',]:
#                return data

        raise forms.ValidationError("Image must be in .jpg format")
        return data


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
