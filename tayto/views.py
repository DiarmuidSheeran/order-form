from django.shortcuts import render, redirect
from orderForm.models import taytoOrder, OrderProduct
from tayto.models import taytoProduct, Category

def tayto(request):
    products = taytoProduct.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')
    sort_by = request.GET.get('sort_by', 'category')

    # Filter products by selected category
    if selected_category:
        products = products.filter(category_id=selected_category)

    # Sort products by selected criteria
    if sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'weight':
        products = products.order_by('weight')
    else:  # Default sorting by category
        products = products.order_by('category', 'name')

    # Initialize quantities dictionary
    quantities = {}

    # Retrieve quantities from session if they exist
    if 'quantities' in request.session:
        quantities = request.session['quantities']

    # Update quantities with current GET request values
    for product in taytoProduct.objects.all():
        product_key = str(product.pk)
        if f'quantity_{product_key}' in request.GET:
            quantities[product_key] = request.GET.get(f'quantity_{product_key}', '0')

    # Save the updated quantities back to the session
    request.session['quantities'] = quantities

    # Handle form submission
    if request.method == 'POST':
        order = taytoOrder.objects.create()
        for product in taytoProduct.objects.all():
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
        # Clear the session quantities after submitting the order
        del request.session['quantities']
        return redirect('index')

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'quantities': quantities,
        'sort_by': sort_by,
    }

    return render(request, 'tayto/tayto-order.html', context)
