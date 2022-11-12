from django.urls import path 
from .views import *


app_name = 'sales'
urlpatterns = [
    path('',home_view,name = 'home'),
    path('sales/',SalesView.as_view(),name = 'list'),
    path('sales/<pk>/',SalesDetailView.as_view(),name = 'details')
]


