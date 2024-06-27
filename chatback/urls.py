from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('signup/', views.register, name='signup'),
    path('account/', views.profile, name='account'),
]