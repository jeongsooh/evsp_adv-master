from django.urls import path
from . import views

urlpatterns = [
  path('', views.Ocpp16List.as_view()),
  path('simul/', views.index),
  path('simul/<str:cpnumber>/', views.index),
]