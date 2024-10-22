from django.urls import path
from .views import plan, edit
from . import views

urlpatterns = [
    path('', views.plan, name="plan"),
    path('edit/', views.edit, name="edit"),
    
]