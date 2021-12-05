from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import quote
from random import randint
from django.core.cache import cache

def get_date():
    res = ""
    for i in range(8):
        res += str(randint(0,9))
    return res
def apply_code(request):
    appid = "242"
    redirect_uri = quote("https://app242.acapp.acwing.com.cn/settings/acwing/web/receive_code/")
    scope = "userinfo"

    state = get_date()
    cache.set(state, True, 7200)

    apply_code_url = "https://www.acwing.com/third_party/api/oauth2/web/authorize/"


    return JsonResponse({
        'result': 'success',
        'apply_code_url': apply_code_url+"?appid=%s&redirect_uri=%s&scope=%s&state=%s" % (appid,redirect_uri,scope,state),
    })