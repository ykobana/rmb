# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import logging
from accounts.models import Character, UserAndCharacterLink
from django.views.decorators.csrf import csrf_exempt

@login_required
def profile(request):
    logging.debug("profile() called.")

    # ここで、ユーザとキャラクタ紐づけDBからユーザに紐付いているキャラクタをすべて取得する
    # js側で、forでそれぞれのキャラクタに対して、パラメータと画像を表示する

    # ログインユーザに紐付いているキャラクタ一覧を取得する
    user_and_character_links_obj = UserAndCharacterLink.objects.filter(user_key=request.user)
    logging.debug("UserAndCharacterLink found!")

    # 取得したキャラクタ一覧のキャラクタをすべて取得する
    characters_list = []
    for user_and_character_link_obj in user_and_character_links_obj:
        characters_list.append(Character.objects.get(pk=user_and_character_link_obj.character_key.pk))

    response = {
        "characters_list": characters_list
    }

    return render(request, 'show/profile.html', response)


@login_required
@csrf_exempt
def delete_character(request):
    logging.debug("delete_character() called.")
    response_file_path = 'show/delete_result.html'
    character_id = request.GET['id']
    result_msg=""

    # 指定されたキャラクタを削除する
    # TODO: ユーザに紐付いていない場合に削除できないようにする
    # 見つけたキャラがユーザと紐付いているか？を確認する
    # 1.ログインユーザに紐付いているキャラ一覧を取得する
    # 2.キャラ一覧に含まれるリクエストidと同じpkをもつキャラを取得する
    try:
        logging.debug("character found!")
        user_and_character_links = UserAndCharacterLink.objects.filter(user_key=request.user)
        # ログインユーザがキャラを持っていない
        if user_and_character_links.count() == 0:
            result_msg = "could not delete character because you don't have any character..."
            response = {
                "result_msg": result_msg
            }
            return render(request, response_file_path, response)

        # ログインユーザに紐付いている取得したキャラ一覧に該当するIDのキャラを検索し、削除する
        for user_and_character_link in user_and_character_links:
            character_obj = Character.objects.get(pk=user_and_character_link.character_key.pk)
            logging.debug("character_obj.pk: " + str(character_obj.pk))
            logging.debug("character_id: " + str(character_id))

            if int(character_obj.pk) == int(character_id):
                character_obj.delete()
                logging.debug("character deleted!")
                result_msg = "succeeded to delete character!"

    except Character.DoesNotExist:
        logging.debug("character not found...")
        result_msg = "could not delete character because your request is incorrect.."

    logging.debug("result_msg: " + result_msg)

    response = {
        "result": result_msg
    }

    return render(request, 'show/delete_result.html', response)



