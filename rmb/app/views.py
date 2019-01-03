from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import User
import logging


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'app/login.html'


def auth(request):
    # リクエストのユーザ名、パスワードを取得する
    postdata = request.body
    username = request.POST['username']
    password = request.POST['password']

    logging.debug("username : %s", username)
    logging.debug("password : %s", password)

    # ユーザ名とパスワードの有効性を検証する
    # 該当するユーザ名があるかを探す
    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        logging.debug("error: Query not exit!!")
        user = None

    if (user is not None) and (password == getattr(user, "password")):
        logging.debug("if ok!!!!") # ここでログイン成功時の場所にリダイレクトする
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        logging.debug("if ng!!!! password is %s, user.password is %s", password, User.password)  # ここでエラー文言を返す

#    return render(request, "login.html", username)
    return redirect("index")  # view内で定義しているメソッドを呼び出す


def index(request):
    return HttpResponse("Success!!")