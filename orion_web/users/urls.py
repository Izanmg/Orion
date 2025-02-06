from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='log'),
    path('register/',views.register,name='registr'),
    path('home/',views.home,name="home"),

]