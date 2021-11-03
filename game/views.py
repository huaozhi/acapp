from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">和平精英</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<img src="https://img1.baidu.com/it/u=119143093,203015299&fm=26&fmt=auto" width=1500>'
    line3 = '<hr>'
    return HttpResponse(line1+line4+line3+line2)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<hr>'
    line3 = '<img src="https://img2.baidu.com/it/u=418285876,2211114287&fm=26&fmt=auto" width=1500>'
    line4 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1+line4+line2+line3)
