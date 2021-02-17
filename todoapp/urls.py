from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('new/',New.as_view(), name='new'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]
