from django.shortcuts import render, redirect
from orderForm.models import taytoOrder
from tayto.models import taytoProduct
from orderForm.forms import taytoOrderForm

def tayto(request):
    products = taytoProduct.objects.all()

    if request.method == 'POST':
        form = taytoOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()  # Save the order first to get an ID

            # Associate selected products with the order
            selected_products = form.cleaned_data['products']
            order.products.set(selected_products)  # Set the many-to-many relation

            return redirect('index')  # Redirect to 'index' upon successful submission
    else:
        form = taytoOrderForm()

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'tayto/tayto-order.html', context)
