from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    # Displays columns for quick identification of quotes
    list_display = ('id', 'name', 'company', 'product', 'quantity', 'unit', 'status', 'created_at')
    # Filters by status (Pending, Approved, Rejected) and unit type
    list_filter = ('status', 'unit', 'created_at')
    # Search quotes by contact details
    search_fields = ('name', 'company', 'email', 'phone')