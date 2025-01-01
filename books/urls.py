from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<slug:slug>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
