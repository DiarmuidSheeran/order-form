from django.urls import path
from . import views

urlpatterns = [
    path('walkers/', views.walkers, name="walkers"),
]   
