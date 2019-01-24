from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone_number']
        widgets = {
            'phone_number': forms.TimeInput(format='%H:%M', attrs={'placeholder': 'Some help text'}),
        }
        exclude = ['created', ]

