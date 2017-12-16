from django import forms

from .models import Customer


class AccountForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = (
            'user_name',
            'password'
        )
