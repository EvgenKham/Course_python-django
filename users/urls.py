from django.urls import path, re_path
from django.views.generic import TemplateView

from users.views import LogoutView, LoginFormView, UserRegistrationForm


urlpatterns = [
    # path('', TemplateView.as_view(template_name='base.html')),
    # path('login', register_user),
    re_path(r'^register/$', UserRegistrationForm.as_view(), name='register'),
    re_path(r'^login/$', LoginFormView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
]
