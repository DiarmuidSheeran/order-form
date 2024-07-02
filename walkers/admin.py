from django.contrib import admin
from .models import walkersProduct, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class walkersProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'productCode', 'quantity', 'weight', 'barcode', 'caseCount')
    search_fields = ('name', 'productCode', 'barcode', 'category__name')  # Updated to allow search by category name
    list_filter = ('category', 'quantity', 'weight', 'caseCount')
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'productCode', 'barcode', 'category')  # Added category here
        }),
        ('Stock Information', {
            'fields': ('quantity', 'weight', 'caseCount')
        }),
    )

admin.site.register(walkersProduct, walkersProductAdmin)
admin.site.register(Category, CategoryAdmin)