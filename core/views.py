from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product
from .forms import ContactForm
from quotes.forms import QuoteForm

@login_required
def home(request):
    # Force redirect to role checking view
    return redirect('core:login_redirect')

@login_required
def login_redirect(request):
    # Admin goes to Django Admin Panel, Staff goes to Dashboard
    if request.user.is_superuser:
        return redirect('/admin/')
    return redirect('dashboard:home')

def about(request):
    return render(request, 'core/about.html', {
        'title': 'About Us - Green Core Factory Systems'
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Django built-in success message trigger
            messages.success(request, "Your message has been sent successfully! Our sales team will get back to you shortly.")
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {
        'title': 'Contact Us - Green Core Factory Systems',
        'form': form
    })

def services(request):
    # Fetch all categories and active products from the SQLite database
    categories = Category.objects.all()
    products = Product.objects.filter(availability=True)
    
    return render(request, 'core/services.html', {
        'title': 'Our Products & Services - Green Core',
        'categories': categories,
        'products': products
    })

def request_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your quotation request has been submitted successfully! Check your email for details.")
            return redirect('core:request_quote')
    else:
        form = QuoteForm()
        
    return render(request, 'quotes/request_quote.html', {
        'title': 'Request a Quote - Green Core',
        'form': form
    })