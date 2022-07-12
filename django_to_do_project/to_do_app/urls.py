from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.index, name='home'),
    path('todos/new/', views.new_to_do, name='new'),
]