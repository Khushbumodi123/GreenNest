# urls.py
from django.urls import path
from . import views

app_name = 'profile_page'

urlpatterns = [
    path('profile/', views.prof, name='profile'),
]

