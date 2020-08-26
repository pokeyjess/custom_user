from django import forms
from custom_user.models import MyUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "display_name", "age", "password"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

