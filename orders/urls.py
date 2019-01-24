from django.urls import path, re_path
from orders.views import OrderCreate

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/$', OrderCreate, name='order_create'),
]

