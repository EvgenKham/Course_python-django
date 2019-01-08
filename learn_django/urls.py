"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from my_internet_shop.views import *


urlpatterns = [

    path('admin/', admin.site.urls),
    # path('users', include('users')),
    path('', include('my_internet_shop.urls')),


    # path("users/", views.users),
    # path("users/<int:id>/<name>/", views.users),
    #
    # path("", views.index),
    # re_path(r"^about", TemplateView.as_view(template_name="about.html")),
    # re_path(r"^contacts", TemplateView.as_view(template_name="contacts.html")),

]
