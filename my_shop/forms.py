from django import forms

cities = (('Minsk', 'Минск'), ('Gomel', 'Гомель'), ('Brest', 'Брест'))


class TestForm(forms.Form):
    city = forms.TypedChoiceField(choices=cities)

    name = forms.CharField(initial='Your name',
                           max_length=10,
                           help_text='10 characters max',
                           error_messages={'required': 'Please enter your name'}
                           )

    email = forms.EmailField(widget=forms.EmailInput(
                                attrs={
                                    'class': 'contact-form',
                                    'id': 'new_label_42'
                                }))
