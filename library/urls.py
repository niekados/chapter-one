from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_library, name='my_library'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),
]
