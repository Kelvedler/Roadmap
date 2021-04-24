from django.urls import path
from basic_forms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_name_view, name='form_name'),
]
