from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='log'),
    path('register/',views.register,name='registr'),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout"),

]