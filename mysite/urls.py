from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('3d/', views.post, name='3d')
]