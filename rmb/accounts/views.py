from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import User
import logging
from django.db import DatabaseError


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'accounts/login.html'


def authenticate(request):
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
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        logging.debug("error: Query not exit!!")
        user = None

    if (user is not None) and (user.check_password(password)):
        logging.debug("if ok!!!!")  # ここでログイン成功時の場所にリダイレクトする
        return render(request, 'accounts/main.html', {
            'username': username
        })
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す
        return render(request, 'accounts/login.html', {
            'error': 'Your usernamne and password did not match. Please try again.'
        })


def register(request):
    # リクエストのユーザ名、パスワード、Eメールアドレスを取得する
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    # 取得した情報で登録する
    # TODO:失敗したらエラーを返す（すでに同じユーザまたはEmailアドレスが存在している）
    new_user = User(username=username, email=email)
    new_user.set_password(password)

    try:
        new_user.save()
        logging.debug("database register success!!!!")
        return redirect("main")
    except DatabaseError:
        logging.debug("database error occurred!!!!")
        return render(request, 'accounts/register.html', {
            'error': 'database error occurred'
        })
