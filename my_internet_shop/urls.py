from django.urls import path, re_path
from my_internet_shop.views import *

urlpatterns = [
    path('', MobilePhoneList.as_view()),
    re_path(r'^(?P<slug>[-\w]+)$', MobilePhoneSingle.as_view(), name='detail')
    ]

