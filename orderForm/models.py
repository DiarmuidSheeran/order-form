# models.py
from django.db import models
from tayto.models import taytoProduct
from django.utils import timezone

class taytoOrder(models.Model):
    products = models.ManyToManyField(taytoProduct, through='OrderProduct', related_name='orders')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.pk}"

    def display_products(self):
        return ", ".join([f"{item.product.name} (Qty: {item.quantity})" for item in self.orderproduct_set.all()])
    display_products.short_description = 'Products'

class OrderProduct(models.Model):
    order = models.ForeignKey(taytoOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(taytoProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

