from django.shortcuts import render

# Create your views here.
def stafford(request):
    return render(request, 'stafford/stafford-order.html')