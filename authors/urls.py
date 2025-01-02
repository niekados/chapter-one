from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_list, name='authors_list'),
    path('add_author/', views.add_author, name='add_author'),
]
