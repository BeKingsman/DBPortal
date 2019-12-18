from django.urls import path
from . import views

urlpatterns = [

    path('upload/',views.upload_excel,name = 'upload_excel'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
