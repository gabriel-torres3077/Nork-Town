from django.contrib import admin
from django.urls import path, include
from .views import home, create, update, edit, delete, create_car, build_car, delete_car, update_car

urlpatterns = [
    path('', home),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name="update"),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),

    path('create_car/<int:id>', create_car, name='create_car'),
    path('delete_car/<int:id>', delete_car, name='delete_car'),
    path('build_car/<int:id>', build_car, name='build_car'),
    path('update_car/<int:id>', update_car, name='update_car')
]