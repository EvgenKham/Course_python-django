from django.shortcuts import render, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic.edit import FormView
from django.views.generic.base import View

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, request


class LogoutView(View):
    """Класс для выхода из учетной записи"""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass


class LoginFormView(FormView):
    """Класс для авторизации пользователей"""
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        pass


class UserRegistrationForm(FormView):
    """Класс для регистрации новых пользователей"""
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = "/user/login/"

    def form_valid(self, form):
        form.save()
        return super(UserRegistrationForm, self).form_valid(form)
        pass


