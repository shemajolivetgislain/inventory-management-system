from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('staff/', views.staff, name='home'),
]
