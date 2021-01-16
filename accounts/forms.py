#check for unique username and email
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                }
        )
    )
    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password",
                }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username is invalid, please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use, please use another.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
        }))
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        return username