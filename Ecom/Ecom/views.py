from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def reg(request):
    return render(request, 'reg.html')
def login(request):
    return render(request, 'login.html')
def productView(request):
    return HttpResponse("Product View Page ")
def checkout(request):
    return render(request, 'checkout.html')
