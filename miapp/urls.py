from django.urls import path
from . import views

urlpatterns = [
    path('', views.love_page, name='love_page'),
]