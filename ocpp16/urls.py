from django.urls import path
from . import views

urlpatterns = [
  path('', views.lobby),
  path('<str:cpnumber>/', views.lobby),
]