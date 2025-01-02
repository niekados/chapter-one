from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_list, name='authors_list'),
    path('add/', views.add_author, name='add_author'),
    path('manage_authors/', views.owner_manage_authors, name='manage_authors'),
    path('edit/<int:author_id>/', views.edit_author, name='edit_author'),
    path('delete/<int:author_id>/', views.delete_author, name='delete_author'),
    path(
        'confirm_delete/<int:author_id>/',
        views.confirm_delete_author,
        name='confirm_delete_author'
    ),
]
