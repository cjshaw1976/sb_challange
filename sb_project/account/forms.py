from django import forms

from django.core.exceptions import ValidationError

from .models import Customer

import re

# Todo customer must be 16 years or older

class AccountForm(forms.ModelForm):
    VALID_IMAGE_EXTENSIONS = [
        ".jpg",
        ".pdf",
    ]

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
        # Check that images are included and have either jpg or pdf extension
        data = self.cleaned_data['headshot_image']

        if data:
            if any([data.name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                return data

        raise ValidationError("Image must have .jpg or .pdf extension")
        return data


    def clean_residence_image(self):
        # Check that images are included and have either jpg or pdf extension
        data = self.cleaned_data['residence_image']

        if data:
            if any([data.name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                return data

        raise ValidationError("Image must have .jpg or .pdf extension")
        return data


    def clean_signature_image(self):
        # Check that images are included and have either jpg or pdf extension
        data = self.cleaned_data['signature_image']

        if data:
            if any([data.name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                return data

        raise ValidationError("Image must have .jpg or .pdf extension")
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
