from django.db import models
from datetime import date
from my_shop.models import MobilePhone, Projector, TV


class Order(models.Model):
    first_name = models.CharField(verbose_name='Ваше имя', max_length=200)
    phone_number = models.CharField(verbose_name='Ваш номер телефона', max_length=200)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(MobilePhone, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    # sess_id = models.CharField(max_length=320, blank=True, db_index=True, verbose_name='Сессия')
    # created_at = models.DateTimeField(default=date.today())

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

