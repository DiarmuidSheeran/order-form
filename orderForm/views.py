from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from weasyprint import HTML
from .models import taytoOrder, walkersOrder
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    """
    Renders the user login page.
    User is prompted to enter a valid username
    User is prompted to enter a valid password
    Request is sent to authenticate user
    If request is successful user is redirected to index page.
    If request is denied (doesnt exsit on database) login page is render
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'orderForm/login.html')

@login_required(login_url='login')
def logoutUser(request):
    """
    Redirects user to landing page
    """
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    return render(request, 'orderForm/index.html')

@login_required(login_url='landing')
def savedOrders(request):
    return render(request, 'orderForm/saved_orders.html')

@login_required(login_url='login')
def taytoSavedOrders(request):
    orders = taytoOrder.objects.all().order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orderForm/tayto_saved_orders.html', context)

@login_required(login_url='login')
def walkersSavedOrders(request):
    orders = walkersOrder.objects.all().order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orderForm/walkers_saved_orders.html', context)

@login_required(login_url='login')
def generate_pdf(request, order_id):
    order = get_object_or_404(taytoOrder, id=order_id)
    html_string = render_to_string('orderForm/order_pdf.html', {'order': order})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'
    return response

@login_required(login_url='login')
def delete_order(request, order_id):
    order = get_object_or_404(taytoOrder, id=order_id)
    order.delete()
    return redirect('tayto_saved_orders')

@login_required(login_url='login')
def walkers_generate_pdf(request, order_id):
    order = get_object_or_404(walkersOrder, id=order_id)
    html_string = render_to_string('orderForm/walkers_order_pdf.html', {'order': order})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'
    return response

@login_required(login_url='login')
def walkers_delete_order(request, order_id):
    order = get_object_or_404(walkersOrder, id=order_id)
    order.delete()
    return redirect('walkers_saved_orders')
