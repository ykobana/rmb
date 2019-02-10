# Create your views here.
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.core import serializers
from .models import Chat


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
