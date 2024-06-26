# admin.py
from django.contrib import admin
from .models import taytoOrder, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
    readonly_fields = ('product', 'quantity')

class taytoOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_products')
    search_fields = ('id',)
    inlines = [OrderProductInline]

    def display_products(self, obj):
        return ", ".join([f"{item.product.name} (Qty: {item.quantity})" for item in obj.orderproduct_set.all()])
    display_products.short_description = 'Products'

admin.site.register(taytoOrder, taytoOrderAdmin)


