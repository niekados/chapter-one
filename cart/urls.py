from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path(
        'remove/<int:book_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
]
