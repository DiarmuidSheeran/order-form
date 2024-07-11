from django.urls import path
from . import views

urlpatterns = [
    path('stafford/', views.stafford, name="stafford"),
]   