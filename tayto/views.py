from django.shortcuts import render

def tayto(request):
    """
    Renders the index page.
    """
    return render(request, 'tayto/tayto-order.html')
