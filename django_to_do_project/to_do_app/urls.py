from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.index, name='home'),
    path('todos/new', views.new_to_do, name='new'),
    path('todos/<int:id>', views.details, name='details'),
    path('todos/<int:id>/edit', views.edit, name='edit'),
    path('todos/<int:id>/delete', views.delete_item, name='delete_item'),
    path('log-in', views.log_in, name='log_in'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('log-out', views.log_out, name='log_out'),
]