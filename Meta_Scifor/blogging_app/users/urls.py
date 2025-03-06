from django.urls import path
from .views import register, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    # path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]
