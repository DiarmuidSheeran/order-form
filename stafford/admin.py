from django.contrib import admin
from .models import staffordProduct, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class staffordProductAdmin(admin.ModelAdmin):
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

admin.site.register(staffordProduct, staffordProductAdmin)
admin.site.register(Category, CategoryAdmin)
