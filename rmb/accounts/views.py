from django.shortcuts import render, redirect
from .models import User
import logging
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as django_login
from menu.models import Chat
from django.contrib.auth.hashers import make_password


def login(request):
    logging.debug("login() called.")
    return render(request, 'accounts/login.html', {})


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
        user.username = username
        django_login(request, user)

        # チャットの履歴を取得する
        chat_list = Chat.objects.order_by('-date')[:50]

        context = {
            'username': username,
            "chat_list": chat_list
        }

        return render(request, 'menu/menu.html', context)

    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す
        login_form = LoginForm()
        return render(request, 'accounts/login.html', {
            'error': 'Your username and password did not match. Please try again.'
        })


def register(request):
    logging.debug("register() called.")

    if request.method == 'POST':
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


'''
        # リクエストのユーザ名、パスワード、Eメールアドレスを取得する
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # 取得した情報で登録する
        new_user = User.objects.create_user(username=username, password=password, email=email)

        try:
            new_user.save()
            logging.debug("database register success!!!!")
            return render(request, 'accounts/registration.html', {
                'result': 'registration succeeded!'
            })
        except DatabaseError:
            logging.debug("database error occurred!!!!")
            return render(request, 'accounts/registration.html', {
                'result': 'database error occurred'
            })
'''


def logout(request):
    request.session.flush()
    return redirect('accounts:login')
