"""authot:
   data:
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 获取手机验证码
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^get_login_captcha/$', views.get_login_captcha, name='get_captcha'),
    url(r'^check_login_captcha/$', views.check_login_captcha, name='check_captcha'),

    ]