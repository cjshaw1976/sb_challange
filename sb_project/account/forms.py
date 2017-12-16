from django import forms

from django.core.exceptions import ValidationError

from .models import Customer

from datetime import datetime, timedelta
import re

# Todo customer must be 16 years or older

class AccountForm(forms.ModelForm):
    VALID_IMAGE_EXTENSIONS = [
        ".jpg",
        ".pdf",
    ]

    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        # Check password is valid format
        # Must be at least 6 character and include at least one of each of the following
        # Upper and lower case characters, digits and special character
        data = self.cleaned_data['password']

        if not re.match("^(?=.*[!@#$%^&*()_+-=?|:;'/\])(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{6,15}$", data):
            # Does not match
            raise ValidationError('Invalid Password. Must be between 6 and 15 characters, include upper and lower case character, digits and special charters but no spaces.')

        # Remember to always return the cleaned data.
        return data

    def clean_id_number(self):
        # Check id number is valid format
        # 2 digits, optional space or minus, 6 or 7 digits, one letter, 2 digits
        data = self.cleaned_data['id_number']

        if not re.match("^(?:\d{2}(?:\s|\-)\d{6,7}[a-zA-Z]\d{2})|(?:\d{8,9}[a-zA-Z]\d{2})$", data):
            # Does not match
            raise ValidationError('Invalid ID Format')

        # Remember to always return the cleaned data.
        return data

    def clean_birth_date(self):
        # Check that person is 16 years or older
        now = datetime.now()
        ago = datetime(now.year - 16, now.month, now.day)
        data = self.cleaned_data['birth_date']

        # if datetime(birthdate) > ago
        # raise ValidationError('Account Holder must be atleast 16 years old')
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
            'password',
            'first_name',
            'last_name',
            'birth_date',
            'id_number',
            'phone_number',
            'email_address',
            'physical_address',
            'headshot_image',
            'residence_image',
            'signature_image',
        )
