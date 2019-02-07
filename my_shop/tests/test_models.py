from django.test import TestCase
from my_shop.models import Category, MobilePhone


class TestMobilePhoneModel(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(name='Смартфоны', slug='smartfony')

        self.phone = MobilePhone.objects.create(category=self.cat,
                                                name='Apple X',
                                                slug='apple-x',
                                                count=67,
                                                operation_system='WindowsPhone',
                                                slug_o_p='windowsphone',
                                                ram=4,
                                                battery=3700,
                                                price=3245.0)

        self.test_phone = MobilePhone.objects.get(name='Apple X')
        pass

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_name_max_length_mobile_phone(self):
        max_length = self.test_phone._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
        pass

    def test_get_absolute_url_mobile_phone(self):
        self.assertEquals(self.test_phone.get_absolute_url(), '/phone/apple-x/')

    def test_str_mobile_phone(self):
        self.assertEquals(self.test_phone.__str__(), 'Apple X')
