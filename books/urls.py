from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
