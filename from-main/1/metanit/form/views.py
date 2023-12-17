from django.shortcuts import render
from .forms import OrderForm

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            house_number = form.cleaned_data['house_number']
            apartment_number = form.cleaned_data['apartment_number']

            # Формирование сообщения
            message = f"{first_name} {last_name}, проверьте адрес доставки:\n{country}\n{city}\n{street} {house_number}\nКвартира {apartment_number}"

            # Передача данных в шаблон
            return render(request, 'order.html', {'message': message})

    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})
