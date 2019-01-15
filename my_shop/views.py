from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from my_shop.models import *


class Index(ListView):
    """    Стартавая view, для представления всех категорий и всех товаров    """
    template_name = 'base.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'

    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['mobile_phones'] = MobilePhone.objects.all()
        return context
        pass


class CategorySinger(DetailView):
    """     View для представления всех товаров из категории    """
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        context['category'] = Category.objects.get(slug="mobilnye-telefony")
        context['mobile_phones'] = MobilePhone.objects.all()
        return context
        pass


# class MobilePhoneList(ListView):
#     template_name = 'mobile_phones_list.html'
#     queryset = MobilePhone.objects.all()
#     context_object_name = 'mobile_phones'
#
#     # model = Category
#     model = MobilePhone
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['categories'] = Category.objects.all()
#         context['mobile_phones'] = MobilePhone.objects.all()
#         return context
#         pass


class MobilePhoneSingle(DetailView):
    """     View для представления подрабной информации о мобильном телефоне    """
    model = MobilePhone
    template_name = 'mobile_phone_details.html'
    context_object_name = 'mobile_phone'
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        context['mobile_phones'] = MobilePhone.objects.all()
        return context
        pass

# class CategorySinger(ListView):
#
#     template_name = 'cat_details.html'
#
#     def get_queryset(self):
#         self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
#         return MobilePhone.objects.filter(category=self.category)
#         pass
#
#     def get_context_data(self, **kwargs):
#         context = super(CategorySinger, self).get_context_data(**kwargs)
#         return context
#         pass
