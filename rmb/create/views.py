# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse
import logging
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Character
from django.contrib.sites.shortcuts import get_current_site


@require_POST
@csrf_exempt
def upload_graffiti(request):
    logging.debug("upload_graffiti() called.")
    # アップロードされたファイルを保存する。
    upload_file = request.FILES['graffiti']
    upload_image = Character(graffiti_image=upload_file)
    upload_image.save()

    # ファイルにアクセスするためのURLを作成する。
    current_site = get_current_site(request)
    domain = current_site.domain
    download_url = '{0}://{1}/{2}'.format(
        request.scheme,
        domain,
        upload_image.graffiti_image.url,
    )

    # URLを文字列として返す。
    return HttpResponse(download_url, content_type="text/plain")
