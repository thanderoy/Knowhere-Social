from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        data = self.cleaned_data
        if data.get("password") != data.get("password2"):
            raise forms.ValidationError("Passwords don't match")
        return data.get("password2")

    def clean_email(self):
        data = self.cleaned_data
        if User.objects.filter(email=data.get("email")).exists():
            raise forms.ValidationError("Email already in use.")
        return data.get("email")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        data = self.get("email")
        qs = User.objects.filter(
            email=data.get("email")
        ).exlude(id=self.instance.id)

        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return data.get("email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]
