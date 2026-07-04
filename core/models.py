from django.db import models

# 1. Category Model (Stores paper categories like Kraft, Duplex, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# 2. Product Model (Stores individual paper grades linked to a category)
class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    gsm = models.CharField(max_length=50, help_text="e.g. 120 - 250 GSM")
    size = models.CharField(max_length=100, help_text="e.g. Deckle 2400mm")
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# 3. Contact Model (Stores messages sent via the contact page)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"