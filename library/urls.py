from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_library, name='my_library'),
]
