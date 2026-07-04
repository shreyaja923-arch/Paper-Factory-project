from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quotes.models import Quote
from orders.models import Order

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