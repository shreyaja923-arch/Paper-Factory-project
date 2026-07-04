from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Columns to view order details
    list_display = ('id', 'quote', 'stage', 'tracking_number', 'estimated_delivery', 'created_at')
    # Filters based on manufacturing stage
    list_filter = ('stage', 'estimated_delivery')
    # Search by tracking number, or customer name/company from the linked Quote
    # (Django uses double underscores '__' to search across related tables!)
    search_fields = ('tracking_number', 'quote__company', 'quote__name')