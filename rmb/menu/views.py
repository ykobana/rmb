# Create your views here.
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.core import serializers
from .models import Chat
from datetime import datetime
import logging


def main(request):
    session = request.session.get('username')
    if session is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('accounts:login')

    return render(request, 'menu/menu.html', {})


def get_chat_list(request):
    # チャットの履歴を取得する
    chat_list = Chat.objects.order_by('-date')[:50]
    return JsonResponse(serializers.serialize('json', chat_list), safe=False)


def post_chat_message(request):
    logging.debug("post_chat_message() called.")

    if request.method == 'POST':
        post_json = request.POST
        logging.debug(post_json)

        post_chat_model = Chat.objects.create(date=datetime.now(),
                                              name=post_json['username'],
                                              message=post_json['message'])
        post_chat_model.save()

    ret = {"data": "param1"}
    return JsonResponse(ret)

