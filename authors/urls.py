from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_list, name='authors_list'),
    path('add/', views.add_author, name='add_author'),
    path('edit/<int:author_id>/', views.edit_author, name='edit_author'),
]
