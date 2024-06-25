from django.db import models
from tayto.models import taytoProduct

class taytoOrder(models.Model):
    products = models.ManyToManyField(taytoProduct, related_name='orders')

    def __str__(self):
        return f"Order {self.pk}"


