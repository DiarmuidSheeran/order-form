from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('saved_orders/', views.savedOrders, name="saved_orders"),
    path('tayto_saved_orders/', views.taytoSavedOrders, name="tayto_saved_orders"),
    path('walkers_saved_orders/', views.walkersSavedOrders, name="walkers_saved_orders"),
    path('order/<int:order_id>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('walkers_order/<int:order_id>/pdf/', views.walkers_generate_pdf, name='walkers_generate_pdf'),
    path('walkers_order/<int:order_id>/delete/', views.walkers_delete_order, name='walkers_delete_order'),
]
