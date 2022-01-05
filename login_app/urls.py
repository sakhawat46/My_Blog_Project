from django.contrib.auth import login, logout
from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change/',views.user_change, name='user_change'),
    path('password/',views.password_change, name='password_change'),
    path('add-profile/', views.add_profile_pic, name='add_profile_pic'),
    path('change-profile', views.change_pro_pic, name='change_pro_pic'),
]