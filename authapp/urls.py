from django.urls import path
from authapp import views

app_name = "authapp"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forget-password/', views.forget_password, name='forget_password'),
]