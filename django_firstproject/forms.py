from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )