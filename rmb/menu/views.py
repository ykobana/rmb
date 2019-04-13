# Create your views here.
from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from .models import Chat
from datetime import datetime
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import json

user = get_user_model()

@login_required
def main(request):
    logging.debug("main() called.")
    # チャットの履歴を取得する
    chat_list = Chat.objects.order_by('-date')[:50]

    context = {
        "chat_list": chat_list
    }
    return render(request, 'menu/menu.html', context)


@login_required
def chat_message(request):
    logging.debug("chat_message() called.")

    if request.method == 'POST':
        logging.debug("chat_message(): POST called.")
        post_json = request.POST
        logging.debug(post_json)

        name = request.user.username
        logging.debug("name: %s", name)

        post_chat_model = Chat.objects.create(date=datetime.now(),
                                              name=name,
                                              message=post_json['message'])
        post_chat_model.save()

        return HttpResponse(status=204)

    if request.method == 'GET':
        logging.debug("chat_message(): GET called.")
        # チャットの履歴を取得する
        chat_list = Chat.objects.order_by('-date')[:50]
        json_chat_list = serializers.serialize('json', chat_list)
        logging.debug("json_chat_list: %s", json_chat_list)
        return JsonResponse(json_chat_list, safe=False)

    logging.debug("chat_message(): Bad request.")
    return HttpResponseBadRequest
