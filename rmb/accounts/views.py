from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import User
from django.template import loader
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
        template = loader.get_template('accounts/login.html')
        context = {
            'error': 'POST error occurred!',
        }
        return HttpResponse(template.render(context, request))

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
        return redirect("index")  # view内で定義しているメソッドを呼び出す
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す
        template = loader.get_template('accounts/login.html')
        context = {
            'error': 'Your usernamne and password did not match. Please try again.',
        }
        return HttpResponse(template.render(context, request))


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
        return redirect("index")
    except DatabaseError:
        logging.debug("database error occured!!!!")
        template = loader.get_template('accounts/register.html')
        context = {
            'error': 'database error occured',
        }
        return HttpResponse(template.render(context, request))


def index(request):
    return HttpResponse("Success!!")