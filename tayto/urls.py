from django.urls import path
from . import views

urlpatterns = [
    path('tayto/', views.tayto, name="tayto"),
]   
