from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        # The fields that match our Quote model attributes
        fields = ['name', 'company', 'email', 'phone', 'product', 'quantity', 'unit', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Warehouse 3, Port Zone, City'}),
        }