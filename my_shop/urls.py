from django.urls import path, re_path
from my_shop.views import Index, CategorySinger, MobilePhoneSingle, ProjectorSinger, TVSinger

urlpatterns = [
    path('', Index.as_view(), name='index'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', CategorySinger.as_view(), name='category_detail'),
    re_path(r'^phone/(?P<slug>[-\w]+)/$', MobilePhoneSingle.as_view(), name='phone_detail'),
    re_path(r'^projector/(?P<slug>[-\w]+)$', ProjectorSinger.as_view(), name='projector_detail'),
    re_path(r'^tv/(?P<slug>[-\w]+)$', TVSinger.as_view(), name='tv_detail'),
    ]

