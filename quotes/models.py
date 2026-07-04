from django.db import models

# Choices for the quotation status
STATUS_CHOICES = [
    ('PENDING', 'Pending Review'),
    ('APPROVED', 'Approved (Convert to Order)'),
    ('REJECTED', 'Rejected'),
]

# Choices for quantity units
UNIT_CHOICES = [
    ('MT', 'Metric Tons (MT)'),
    ('Rolls', 'Rolls'),
    ('Sheets', 'Sheets'),
]

class Quote(models.Model):
    # Customer contact details
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Material specs (linking to the Product model in the 'core' app)
    product = models.ForeignKey('core.Product', on_delete=models.SET_NULL, null=True, related_name='quotes')
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='MT')
    
    # Delivery info
    location = models.CharField(max_length=255)
    
    # Metadata & Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote #{self.id} - {self.company} ({self.product.name if self.product else 'Unknown Grade'})"