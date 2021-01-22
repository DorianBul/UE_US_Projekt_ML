from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from django.http import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

import sys
from .activityLogger import dbManager

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        userName = form.cleaned_data.get("username")
        # print("form_valid signup {}".format(userName))
        dbManager.AddRegisterRecord(userName)
        return super().form_valid(form)


class AuthForm(AuthenticationForm):
    success_url = reverse_lazy("")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def confirm_login_allowed(self, user):
        userName = self.cleaned_data.get('username')
        # print("confirm_login_allowed {}".format(userName))
        dbManager.AddActionRecord(userName, "LOG IN", "OK")
        return super().confirm_login_allowed(user)

    def get_invalid_login_error(self):
        userName = self.cleaned_data.get('username')
        # print("get_invalid_login_error {}".format(userName))
        dbManager.AddActionRecord(userName, "LOG IN", "ERROR")
        return super().get_invalid_login_error()


@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    print("User {} logged out".format(str(user)))
    dbManager.AddActionRecord(str(user), "LOG OUT", "NULL")
    pass

