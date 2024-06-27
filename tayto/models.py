from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class taytoProduct(models.Model):
    name = models.CharField(max_length=254)
    quantity = models.IntegerField(null=True, blank=True)
    productCode = models.CharField(null=True, blank=True, max_length=254)
    weight = models.IntegerField(null=True, blank=True)
    barcode = models.CharField(null=True, blank=True, max_length=254)
    caseCount = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Tayto Product"
        verbose_name_plural = "Tayto Products"