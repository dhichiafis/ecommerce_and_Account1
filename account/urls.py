from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
app_name='account'
urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('homepage',views.homepage,name='homepage'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('register/',views.user_registration,name='register'),
    

]