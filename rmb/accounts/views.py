from django.shortcuts import render, redirect, reverse
from .models import User
import logging
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def login(request):
    logging.debug("login() called.")
    return render(request, 'accounts/login.html', {})


@require_POST
def auth(request):
    logging.debug("authenticate() called.")
    try:
        # リクエストのユーザ名、パスワードを取得する
        username = request.POST['username']
        password = request.POST['password']
    except:
        logging.debug("POST error")  # ここでエラー文言を返す
        return render(request, 'accounts/login.html', {
            'error': 'POST error occurred!'
        })

    logging.debug("username : %s", username)
    logging.debug("password : %s", password)

    # ユーザ名とパスワードの有効性を検証する
    # 該当するユーザ名があるかを探す
    user = authenticate(request, username=username, password=password)

    if user is not None:
        logging.debug("if ok!!!! password is %s, user.password is %s", password, User.password)  # ここでログイン成功時の場所にリダイレクトする
        request.session['username'] = username  # セッションIDを作成する
        logging.debug("session: %s", request.session['username'])
        django_login(request, user)
        return redirect(reverse('menu:main'))

    else:
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す
        return render(request, 'accounts/login.html', {
            'error': 'Your username and password did not match. Please try again.'
        })


@require_POST
def register(request):
    logging.debug("register() called.")

    registration_form = RegistrationForm(request.POST)
    if registration_form.is_valid():
        user_info = registration_form.save(commit=False)
        user_info.password = make_password(registration_form.cleaned_data['password'])
        user_info.save()
        logging.debug("database register success!!!!")
        return render(request, 'accounts/registration.html', {
            'result': 'registration succeeded!'
        })

    logging.debug("database error occurred!!!!")
    logging.debug("error: %s", registration_form.errors)
    for field in registration_form:
        for error in field.errors:
            logging.debug("%s", error)

    return render(request, 'accounts/registration.html', {
        'result': registration_form.errors
    })


@login_required
def logout(request):
    request.session.flush()
    return redirect('accounts:login')
