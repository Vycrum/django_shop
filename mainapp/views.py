from django.shortcuts import render
import os

# Create your views here.
def main(request):
    user_login = os.getlogin()
    context = {'user': user_login}
    return render(request, 'mainapp/index.html', context)


def products(request):
    product_items = os.listdir('./mainapp/templates/mainapp/catalog/')
    product_items = [(os.path.splitext(item)[0], count+1) for count, item in enumerate(product_items)]
    context = {'products': product_items}
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')