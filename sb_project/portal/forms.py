from django import forms

from account.models import Customer


class AccountForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    # Override clean so avoid default error message
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = Customer
        fields = (
            'user_name',
            'password'
        )
