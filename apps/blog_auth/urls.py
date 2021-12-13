from django.urls import path
#from django.conf.urls import url
from . import views

app_name='apps.blog_auth'

urlpatterns = [
    path("/login", Login.as_view(), name="login"),
    path("/logout", Logout.as_view(), name="logout"),
    path(r'^registro/$', SignUpView.as_view(), name="sign_up"),
]