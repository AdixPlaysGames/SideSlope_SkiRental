from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.items, name='items'),
    path('<int:pk>/rent/', views.rent_item, name='rent_item')
]