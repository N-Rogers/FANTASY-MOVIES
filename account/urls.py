from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home,name='Home'),
    path('trial/', views.trial, name='trial'),
    path('profile/', views.profile, name='user-profile'),
    path('register/', views.register, name='Registeruser'),  
    path('login/', auth_view.LoginView.as_view(template_name='account/login.html'), name='Login-user'),
    path('logout/', auth_view.LogoutView.as_view(template_name='account/logout.html'), name='Logout'),
    path('resetpassword/', auth_view.PasswordResetView.as_view(template_name='account/password_reset.html'), name='Resetpassword'),
    path('resetpassword/done/', auth_view.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='Resetpassword_done'),
    path('resetpassword-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView .as_view(template_name='account/password_reset_confirm.html'), name='Resetpassword_confirm'),
    path('resetpassword-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='Resetpassword-complete'),

]