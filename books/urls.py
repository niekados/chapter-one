from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<slug:slug>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path(
        'confirm_book_delete/<int:book_id>/',
        views.confirm_delete_book,
        name='confirm_delete_book'
    ),
    path('manage_books/', views.owner_manage_books, name='manage_books'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
