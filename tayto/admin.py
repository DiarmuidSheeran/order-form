from django.contrib import admin
from .models import taytoProduct

class taytoProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'productCode', 'quantity', 'weight', 'barcode', 'caseCount')
    search_fields = ('name', 'productCode', 'barcode')
    list_filter = ('quantity', 'weight', 'caseCount')
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'productCode', 'barcode')
        }),
        ('Stock Information', {
            'fields': ('quantity', 'weight', 'caseCount')
        }),
    )

admin.site.register(taytoProduct, taytoProductAdmin)