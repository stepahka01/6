from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='Email')
    country = forms.CharField(label='Страна', max_length=100)
    city = forms.CharField(label='Город', max_length=100)
    street = forms.CharField(label='Улица', max_length=100)
    house_number = forms.IntegerField(label='Номер дома')
    apartment_number = forms.IntegerField(label='Квартира')
