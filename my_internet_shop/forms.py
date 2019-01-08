from django import forms


class ProductForm(forms.Form):
    name_product = forms.CharField(label="Name product", initial="undefined", max_length=15)
    count = forms.DecimalField(label="Count product", initial=1.1, min_value=1)
