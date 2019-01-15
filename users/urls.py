from django.urls import path, re_path
from django.views.generic import TemplateView

from users.views import LogoutView, LoginFormView, UserRegistrationForm, register_user


urlpatterns = [
    # path('', TemplateView.as_view(template_name='base.html')),
    # path('login', register_user),
    re_path(r'^registration', UserRegistrationForm.as_view()),
    re_path(r'^login', LoginFormView.as_view()),
    re_path(r'^logout', LogoutView.as_view()),
    re_path(r'^main', TemplateView.as_view(template_name='main.html')),
]
