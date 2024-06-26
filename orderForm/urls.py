from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('saved_orders/', views.savedOrders, name="saved_orders"),
    path('tayto_saved_orders/', views.taytoSavedOrders, name="tayto_saved_orders"),
    path('order/<int:order_id>/pdf/', views.generate_pdf, name='generate_pdf'),
]
