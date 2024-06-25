from django.shortcuts import render
from .models import taytoProduct

def tayto(request):
    """
    Renders the index page.
    """
    products = taytoProduct.objects.all()
    return render(request, 'tayto/tayto-order.html', {'products': products})
