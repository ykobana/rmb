from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import User
import logging
from .forms import RegistrationForm
from django.contrib.auth import get_user_model


User = get_user_model()


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'accounts/login.html'


def authenticate(request):
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
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        logging.debug("error: Query not exit!!")
        user = None

    if (user is not None) and (user.check_password(password)):
        logging.debug("if ok!!!!")  # ここでログイン成功時の場所にリダイレクトする
        request.session['username'] = username  # セッションIDを作成する
        logging.debug("session: %s", request.session['username'])
        return render(request, 'menu/menu.html', {
            'username': username
        })
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す
        return render(request, 'accounts/_login.html', {
            'error': 'Your username and password did not match. Please try again.'
        })


def register(request):
    logging.debug("register() called.")

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
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
         'result': 'database error occurred'
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