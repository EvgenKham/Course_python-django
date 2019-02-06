from django.test import TestCase
from my_shop.models import Category, MobilePhone
from my_shop.views import Index, CategorySinger, MobilePhoneSingle, ProjectorSinger, TVSinger

from django.urls import reverse


class TestCategorySinger(TestCase):
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

        self.test_phone = Category.objects.get(id=1)
        pass

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Unforgiven')
        self.assertEqual(resp.status_code, 404)

    # def test_view_uses_correct_template(self):
    #     resp = self.client.get(reverse('category_detail', kwargs={'slug': 'Unforgiven'}))
    #     self.assertTemplateUsed(resp, 'category.html')
