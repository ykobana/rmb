from django import forms
from .models import User


# ユーザ作成フォームを継承
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email")
