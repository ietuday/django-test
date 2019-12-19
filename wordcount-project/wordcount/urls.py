
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('countdsdsdsd/', views.count, name='count')
]
