from django.shortcuts import render, redirect
from orderForm.models import taytoOrder, OrderProduct
from tayto.models import taytoProduct

def tayto(request):
    products = taytoProduct.objects.all()

    if request.method == 'POST':
        order = taytoOrder.objects.create()

        for product in products:
            product_id_field = f"product_id_{product.pk}"
            quantity_field = f"quantity_{product.pk}"

            if product_id_field in request.POST and quantity_field in request.POST:
                try:
                    quantity = int(request.POST[quantity_field])
                    if quantity > 0:
                        product_instance = taytoProduct.objects.get(pk=request.POST[product_id_field])
                        OrderProduct.objects.create(order=order, product=product_instance, quantity=quantity)
                except ValueError:
                    continue

        return redirect('index')

    context = {
        'products': products,
    }

    return render(request, 'tayto/tayto-order.html', context)
