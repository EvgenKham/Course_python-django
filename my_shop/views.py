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
        context['projector'] = Projector.objects.all()
        context['tv'] = TV.objects.all()
        return context
        pass


class CategorySinger(DetailView):
    """     View для представления всех товаров из категории    """
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['mobile_phones'] = MobilePhone.objects.all()
        context['projectors'] = Projector.objects.all()
        context['tvs'] = TV.objects.all()
        return context
        pass


class MobilePhoneSingle(DetailView):
    """     View для представления подрабной информации о мобильном телефоне    """
    model = MobilePhone
    template_name = 'mobile_phone_details.html'
    context_object_name = 'mobile_phone'
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['mobile_phones'] = MobilePhone.objects.all()
        return context
        pass


class ProjectorSinger(DetailView):
    """     View для представления подрабной информации о проекторе   """
    model = Projector
    template_name = 'projector_details.html'
    context_object_name = 'projector'
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['projectors'] = Projector.objects.all()
        return context
        pass


class TVSinger(DetailView):
    """     View для представления подрабной информации о телевизоре   """
    model = TV
    template_name = 'tv_details.html'
    context_object_name = 'tv'
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tvs'] = TV.objects.all()
        return context
        pass
