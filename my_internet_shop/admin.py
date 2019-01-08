from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from my_internet_shop.models import *


class ElectricsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}


class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ['name',
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


admin.site.register(Electrics, ElectricsAdmin)
admin.site.register(MobilePhone, MobilePhoneAdmin)

