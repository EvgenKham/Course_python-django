from django import forms


class ProductForm(forms.Form):
    id = forms.IntegerField(label="Id product", min_value=0)
    name_product = forms.CharField(label="Name product", initial="undefined", max_length=15)
    count = forms.DecimalField(label="Count product", initial=1.1, min_value=1)
    # choice_data = forms.DateField(widget=forms.SelectDateWidget)

