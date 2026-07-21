from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_crop, name='add_crop'),
    path('view/', views.view_crop, name='view_crop'),
    path('edit/<int:id>/', views.edit_crop, name='edit_crop'),
    path('delete/<int:id>/', views.delete_crop, name='delete_crop'),
]
