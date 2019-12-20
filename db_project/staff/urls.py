from django.urls import path
from . import views

urlpatterns = [
    path('mail/',views.mail,name = 'mail'),

    path('home/',views.HomePage,name = 'home-page'),
    path('register/',views.register,name = 'dber-register'),
    path('login/',views.login_view,name = 'dber-login'),
    path('upload/',views.upload_excel,name = 'upload_excel'),
    path('ajax', views.load_cities, name='ajax_load_cities'),
    path('userlist/', views.Dber_list.as_view(), name='user-list'),
    path('userdetail/<int:pk>/', views.Dber_detail.as_view(), name='user-detail'),
]
