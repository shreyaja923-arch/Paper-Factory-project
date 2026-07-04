from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard Home
    path('', views.dashboard_home, name='home'),
    
    # Quote Actions
    path('quotes/<int:quote_id>/approve/', views.approve_quote, name='approve_quote'),
    path('quotes/<int:quote_id>/reject/', views.reject_quote, name='reject_quote'),
    
    # Order Actions
    path('orders/<int:order_id>/advance/', views.advance_order, name='advance_order'),
    
    # Product CRUD Actions
    path('products/', views.manage_products, name='manage_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]