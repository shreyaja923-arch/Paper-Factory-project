from django.shortcuts import render,redirect 
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'core/home.html',{
        'title': 'Green Flow System - Sustainable Industrial Paper Manufacturing'
    })
def about(request):
    return render(request,'core/about.html',{
        'title': 'About Us - Green Core Factory Systems'
    })
def contact(request):
    return render(request,'core/contact.html',{
        'title': 'Contact Us - Green Core Factory Systems'
    })
def services(request):
    return render(request,'core/services.html',{
        'title': 'Our Products & Services - Green Core'
    })
def request_quote(request):
    return render(request,'core/quotes.html',{
        'title': 'Request a Quote - Green Core'
    })