from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from my_shop.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}


class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = [
                    'name',
                    'icon',
                    'slug',
                    'count',
                    'operation_system',
                    'slug_o_p',
                    'ram',
                    'battery',
                    'price'
                    ]
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', ),
                           'slug_o_p': ('operation_system',)}


class ProjectorAdmin(admin.ModelAdmin):
    list_display = [
                    'name',
                    'icon',
                    'slug',
                    'count',
                    'bright',
                    'price'
                    ]
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', )}


class TVAdmin(admin.ModelAdmin):
    list_display = [
                    'name',
                    'icon',
                    'slug',
                    'count',
                    'diagonal',
                    'screen',
                    'slug_screen',
                    'price'
                    ]
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',),
                           'slug_screen': ('screen',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(MobilePhone, MobilePhoneAdmin)
admin.site.register(Projector, ProjectorAdmin)
admin.site.register(TV, TVAdmin)
