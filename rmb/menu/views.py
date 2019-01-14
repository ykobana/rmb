# Create your views here.
from django.shortcuts import render, redirect


def main(request):
    session = request.session.get('username')
    if session is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('accounts:login')

    return render(request, 'menu/menu.html', {})
