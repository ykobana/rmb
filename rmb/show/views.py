# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import logging
from accounts.models import Character, UserAndCharacterLink

@login_required
def profile(request):
    logging.debug("index() called.")

    # ここで、ユーザとキャラクタ紐づけDBからユーザに紐付いているキャラクタをすべて取得する
    # js側で、forでそれぞれのキャラクタに対して、パラメータと画像を表示する

    # ログインユーザに紐付いているキャラクタ一覧を取得する
    try:
        user_and_character_links = UserAndCharacterLink.objects.filter(user_key=request.user)
        logging.debug("UserAndCharacterLink found...!")
    except UserAndCharacterLink.DoesNotExist:
        user_and_character_links = None
        logging.debug("UserAndCharacterLink not found...")

    # 取得したキャラクタ一覧のキャラクタをすべて取得する
    characters_list = []
    for user_and_character_link in user_and_character_links:
        characters_list.append(Character.objects.get(pk=user_and_character_link.character_key.pk))

    response = {
        "characters_list": characters_list
    }

    return render(request, 'show/profile.html', response)
