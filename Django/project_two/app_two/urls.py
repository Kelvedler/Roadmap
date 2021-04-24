from django.urls import path
from app_two import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help_page/', views.help_page, name='help_page'),
    path('users/', views.users, name='users')
]