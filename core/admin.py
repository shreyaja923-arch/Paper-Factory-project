from django.contrib import admin
from .models import Category, Product, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Displays fields as columns in the admin table list
    list_display = ('id', 'name', 'category', 'gsm', 'size', 'availability')
    # Adds a sidebar filter panel on the right
    list_filter = ('category', 'availability')
    # Adds a search bar at the top
    search_fields = ('name', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)  # Protects timestamp from manual edits