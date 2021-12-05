from django.urls import path
from django.urls import include
from game.views.settings.getinfo import getinfo
from game.views.settings.login import signin
from game.views.settings.logout import signout
from game.views.settings.register import register

urlpatterns = [
        path("getinfo/", getinfo, name="setting_getinfo"),
        path("login/", signin, name="settings_login"),
        path("logout/", signout, name="settings_logout"),
        path("register/", register, name="settings_register"),
        path("acwing/", include("game.urls.settings.acwing.index")),
]
