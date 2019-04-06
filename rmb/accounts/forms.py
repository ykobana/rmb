from django import forms
from .models import User


# ログインフォーム
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


# ユーザ作成フォームを継承
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email")
