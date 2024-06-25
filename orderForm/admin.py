from django.contrib import admin
from .models import taytoOrder

class taytoOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_products')
    search_fields = ('id',)  # Add fields you want to search here, 'id' is included as an example
    list_filter = ('products__name',)  # Add filters for products-related fields
    fieldsets = (
        ('Order Information', {
            'fields': ()  # Remove fields 'name', 'productCode', 'barcode' here
        }),
        ('Products', {
            'fields': ('products',)
        }),
    )
    filter_horizontal = ('products',)

    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    display_products.short_description = 'Products'

admin.site.register(taytoOrder, taytoOrderAdmin)
