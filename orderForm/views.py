from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from weasyprint import HTML
from .models import taytoOrder, walkersOrder
from django.template.loader import render_to_string

def index(request):
    return render(request, 'orderForm/index.html')

def savedOrders(request):
    return render(request, 'orderForm/saved_orders.html')

def taytoSavedOrders(request):
    orders = taytoOrder.objects.all().order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orderForm/tayto_saved_orders.html', context)

def walkersSavedOrders(request):
    orders = walkersOrder.objects.all().order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orderForm/walkers_saved_orders.html', context)

def generate_pdf(request, order_id):
    order = get_object_or_404(taytoOrder, id=order_id)
    html_string = render_to_string('orderForm/order_pdf.html', {'order': order})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'
    return response

def delete_order(request, order_id):
    order = get_object_or_404(taytoOrder, id=order_id)
    order.delete()
    return redirect('tayto_saved_orders')

def walkers_generate_pdf(request, order_id):
    order = get_object_or_404(walkersOrder, id=order_id)
    html_string = render_to_string('orderForm/walkers_order_pdf.html', {'order': order})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'
    return response

def walkers_delete_order(request, order_id):
    order = get_object_or_404(walkersOrder, id=order_id)
    order.delete()
    return redirect('walkers_saved_orders')
