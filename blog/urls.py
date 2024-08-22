from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:pk>/', views.post, name='post'),
]