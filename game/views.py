from django.http import HttpResponse

def index(request):
    return HttpResponse("django页面你好！")
