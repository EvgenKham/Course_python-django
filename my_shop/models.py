from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404


def image_folder(instance, filename):
    """
    Метод для коректного отображение картинок
    :param instance: Объект картинка, который добавляется в базу с товаром
    :param filename: Имя файла из которого была довалнена картинка
    :return: Возвращаем строку, где первый агумент - имя новой паки, второй - имя файла
    """
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format("icons", filename)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    pass

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    @staticmethod
    def get_object_by_id_category(cat_id, prod_id):
        category_prod = Category.objects.get(id=cat_id)
        if category_prod.name == "Мобильные телефоны":
            return get_object_or_404(MobilePhone, id=prod_id)
        elif category_prod.name == "Телевизоры":
            return get_object_or_404(TV, id=prod_id)
        elif category_prod.name == "Проекторы":
            return get_object_or_404(Projector, id=prod_id)


class MobilePhone(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default="0000000")
    icon = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Иконка товара",
                             default="my_shop/default_phone.png")
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    operation_system = models.CharField(max_length=100, verbose_name='ОС', db_index=True)
    slug_o_p = models.SlugField(max_length=100, db_index=True, blank=True)
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
        return reverse('phone_detail', kwargs={'slug': self.slug})


class TV(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default="0000000")
    icon = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Иконка товара",
                             default="my_shop/phone_icons/default_phone.png")
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    diagonal = models.FloatField(verbose_name='Диагональ', db_index=True)
    screen = models.CharField(max_length=100, verbose_name='Разрешение', db_index=True)
    slug_screen = models.SlugField(max_length=100, db_index=True, blank=True)
    price = models.FloatField(verbose_name='Цена', db_index=True)

    class Meta:
        ordering = ['name']
        index_together = [
            'id', 'name', 'slug'
        ]
        verbose_name = "Телевизор"
        verbose_name_plural = "Телевизоры"

    def __str__(self):
        return str(self.name)
        pass

    def get_absolute_url(self):
        return reverse('tv_detail', kwargs={'slug': self.slug})


class Projector(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default="0000000")
    icon = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Иконка товара",
                             default="my_shop/phone_icons/default_phone.png")
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    count = models.IntegerField(verbose_name='Количество товаров', db_index=True)
    bright = models.IntegerField(verbose_name='Яркость', db_index=True)
    price = models.FloatField(verbose_name='Цена', db_index=True)

    class Meta:
        ordering = ['name']
        index_together = [
            'id', 'name', 'slug'
        ]
        verbose_name = "Проектор"
        verbose_name_plural = "Проекторы"

    def __str__(self):
        return str(self.name)
        pass

    def get_absolute_url(self):
        return reverse('projector_detail', kwargs={'slug': self.slug})

