from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('msglog-list/', views.msglogList, name='msglog-list'),
  path('msglog-detail/<str:pk>/', views.msglogDetail, name='msglog-detail'),
  path('msglog-create/', views.msglogCreate, name='msglog-create'),
  path('msglog-update/<str:pk>/', views.msglogUpdate, name='msglog-update'),
  path('msglog-delete/<str:pk>/', views.msglogDelete, name='msglog-delete'),
]