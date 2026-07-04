from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quotes.models import Quote
from orders.models import Order
from core.models import Product
from core.forms import ProductForm

@login_required
def dashboard_home(request):
    # 1. Calculate statistics for metrics cards
    total_quotes = Quote.objects.count()
    pending_quotes = Quote.objects.filter(status='PENDING').count()
    active_orders = Order.objects.exclude(stage='DELIVERED').count()
    
    # 2. Fetch items for lists
    quotes = Quote.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')
    
    return render(request, 'dashboard/dashboard.html', {
        'title': 'Admin Dashboard - Green Core Factory Systems',
        'total_quotes': total_quotes,
        'pending_quotes': pending_quotes,
        'active_orders': active_orders,
        'quotes': quotes,
        'orders': orders,
    })

@login_required
def approve_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if quote.status == 'PENDING':
        quote.status = 'APPROVED'
        quote.save()
        
        # Automatically trigger creation of a new manufacturing Order
        Order.objects.create(quote=quote)
        messages.success(request, f"Quote #{quote.id} for {quote.company} approved! Active production order initialized.")
    return redirect('dashboard:home')

@login_required
def reject_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if quote.status == 'PENDING':
        quote.status = 'REJECTED'
        quote.save()
        messages.warning(request, f"Quote #{quote.id} from {quote.company} has been rejected.")
    return redirect('dashboard:home')

@login_required
def advance_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Step-by-step logic transitions for production stages
    if order.stage == 'RECEIVED':
        order.stage = 'PRODUCTION'
        messages.success(request, f"Order #{order.id} shifted to manufacturing floor.")
    elif order.stage == 'PRODUCTION':
        order.stage = 'DISPATCHED'
        # Generate a mock tracking number automatically
        order.tracking_number = f"TRK-GRE-{1000 + order.id}"
        messages.success(request, f"Order #{order.id} marked as Dispatched! Tracking: {order.tracking_number}")
    elif order.stage == 'DISPATCHED':
        order.stage = 'DELIVERED'
        messages.success(request, f"Order #{order.id} logged as Delivered successfully.")
        
    order.save()
    return redirect('dashboard:home')

@login_required
def manage_products(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'dashboard/manage_products.html', {
        'title': 'Manage Products - Green Core',
        'products': products
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New product grade added to the catalog successfully.")
            return redirect('dashboard:manage_products')
    else:
        form = ProductForm()
        
    return render(request, 'dashboard/product_form.html', {
        'title': 'Add New Product - Green Core',
        'form': form,
        'action_name': 'Add New Product'
    })

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{product.name}' specifications updated successfully.")
            return redirect('dashboard:manage_products')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'dashboard/product_form.html', {
        'title': f"Edit Product: {product.name} - Green Core",
        'form': form,
        'action_name': 'Update Specifications',
        'product': product
    })

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_name = product.name
    product.delete()
    messages.warning(request, f"Product '{product_name}' has been deleted from the catalog.")
    return redirect('dashboard:manage_products')
@login_required
def dashboard_home(request):
    # 1. Calculate statistics for metrics cards
    total_quotes = Quote.objects.count()
    pending_quotes = Quote.objects.filter(status='PENDING').count()
    active_orders = Order.objects.exclude(stage='DELIVERED').count()
    
    # 2. Fetch items for lists
    quotes = Quote.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')
    
    # 3. Calculate order stage distribution counts for Chart.js
    stage_received = Order.objects.filter(stage='RECEIVED').count()
    stage_production = Order.objects.filter(stage='PRODUCTION').count()
    stage_dispatched = Order.objects.filter(stage='DISPATCHED').count()
    stage_delivered = Order.objects.filter(stage='DELIVERED').count()
    
    return render(request, 'dashboard/dashboard.html', {
        'title': 'Admin Dashboard - Green Core Factory Systems',
        'total_quotes': total_quotes,
        'pending_quotes': pending_quotes,
        'active_orders': active_orders,
        'quotes': quotes,
        'orders': orders,
        
        # Pass counts to context
        'stage_received': stage_received,
        'stage_production': stage_production,
        'stage_dispatched': stage_dispatched,
        'stage_delivered': stage_delivered,
    })