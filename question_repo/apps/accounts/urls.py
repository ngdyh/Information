"""authot:
   data:
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # TemplateView可以不写视图函数
    # url(r'^register/$', TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    url(r'^register/$', views.Register.as_view(), name='register'),
]