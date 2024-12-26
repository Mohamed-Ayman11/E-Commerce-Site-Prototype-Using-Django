from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    address = forms.CharField(max_length=255)

    class Meta:
        model = Order
        fields = ['customer_name', 'address']
