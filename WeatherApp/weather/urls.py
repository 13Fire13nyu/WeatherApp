from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name=''),
    path('table/', views.table, name='table'),
    path('download/', views.download, name='download'),
]
