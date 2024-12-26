from django.db import models
from django.contrib.auth.models import User

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    image = models.URLField(max_length=2038)  # Changed to URLField for image URLs

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"
    



# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name


class Cart(models.Model):
    
    session_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.session_id}"


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)  # Add cart field
    coffee = models.ForeignKey('coffee.Coffee', on_delete=models.CASCADE)  # Rename product to coffee
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.coffee.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.coffee.name}"