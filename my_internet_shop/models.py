from django.db import models
from django.urls import reverse


class Electrics(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория электроники', db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    pass

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'

    def __str__(self):
        return str(self.name)


class MobilePhone(models.Model):
    category = models.ForeignKey(Electrics, on_delete=models.CASCADE, blank=True, default="0000000")
    name = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    operation_system = models.CharField(max_length=50, verbose_name='ОС', db_index=True)
    slug_o_p = models.SlugField(max_length=50, db_index=True, blank=True)
    ram = models.IntegerField(verbose_name='ОЗУ', db_index=True)
    battery = models.IntegerField(verbose_name='Объем батареи', db_index=True)
    price = models.FloatField(verbose_name='Цена', db_index=True)

    class Meta:
        ordering = ['name']
        index_together = [
            'id', 'name', 'slug'
        ]
        verbose_name = "Мобильный телефон"
        verbose_name_plural = "Мобильные телефоны"

    def __str__(self):
        return str(self.name)
        pass

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Television(models.Model):
    category = models.ForeignKey(Electrics, on_delete=models.CASCADE, blank=True, default="0000000")
    name = models.CharField(max_length=50, db_index=True, verbose_name='Каегории теле')
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    pass


class TV(models.Model):
    category = models.ForeignKey(Television, on_delete=models.CASCADE, blank=True, default="0000000")
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug_name = models.SlugField(max_length=50, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    diagonal = models.FloatField(verbose_name='Диагональ', db_index=True)
    screen = models.CharField(max_length=50, verbose_name='Разрешение', db_index=True)
    slug_screen = models.SlugField(max_length=50, db_index=True, blank=True)
    price = models.FloatField(verbose_name='Цена', db_index=True)

    def __str__(self):
        return str(self.name)
        pass


class Projector(models.Model):
    category = models.ForeignKey(Television, on_delete=models.CASCADE, blank=True, default="0000000")
    name = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    bright = models.IntegerField(verbose_name='Яркость', db_index=True)
    price = models.FloatField(verbose_name='Цена', db_index=True)

    def __str__(self):
        return str(self.name)
