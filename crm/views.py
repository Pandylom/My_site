from django.shortcuts import render
from .models import Order


# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})


def thanks_page(request):
    name = request.GET['name']
    phone = request.GET['phone']
    surname = request.GET['surname']
    return render(request, './thanks.html', {'name': name, 'phone': phone, 'surname': surname})

def login_page(request):
    return render(request, './login.html')
'''
name = request.POST['name']
    phone = request.POST['phone']
    surname = request.POST['surname']
    international = request.POST['international']
    mail = request.POST['mail']
    country = request.POST['country']
    cv = request.POST['cv']
    vakansia = request.POST['vakansia']
    element = Order(order_name=name, order_surname=surname, order_international=international,
                    order_phone=phone, order_mail=mail, order_country=country,
                    order_CV=cv, order_vakansia=vakansia)
    element.save()
'''