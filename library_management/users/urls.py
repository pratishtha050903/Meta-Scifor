from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# ✅ Define urlpatterns before using '+='
urlpatterns = [
    path('register/', views.register, name='register'),
path('register/librarian/', views.register_librarian, name='register_librarian'),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
