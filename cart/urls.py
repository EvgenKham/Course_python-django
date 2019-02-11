from django.urls import path, re_path
from cart.views import *

app_name = 'cart'

urlpatterns = [
    re_path(r'^remove/(?P<category_id>\d+)/(?P<product_id>\d+)/$', CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<category_id>\d+)/(?P<product_id>\d+)/$', CartAdd, name='CartAdd'),
    path('', CartDetail, name='CartDetail'),
    # re_path(r'^my_current_orders/$', OrdersDetail.as_views(), name='my_orders'),
]
