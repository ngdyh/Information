from django.shortcuts import render
from django.views.generic import View
import logging
from .forms import LoginForm, RegisterForm
from .models import User
logger = logging.getLogger('account')


# Create your views here.

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form":form})