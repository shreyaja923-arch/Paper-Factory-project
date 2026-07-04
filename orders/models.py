from django.db import models

# Choices for the order manufacturing stages
STAGE_CHOICES = [
    ('RECEIVED', 'Order Received'),
    ('PRODUCTION', 'In Production'),
    ('DISPATCHED', 'Dispatched / In Transit'),
    ('DELIVERED', 'Delivered'),
]

class Order(models.Model):
    # Link back to the original approved Quote
    # OneToOneField means 1 Quote creates exactly 1 Order
    quote = models.OneToOneField('quotes.Quote', on_delete=models.CASCADE, related_name='order')
    
    # Manufacturing stages tracking
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='RECEIVED')
    
    # Shipment details
    tracking_number = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. TRK-GRE-1004")
    estimated_delivery = models.DateField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} (Quote #{self.quote.id}) - Status: {self.get_stage_display()}"