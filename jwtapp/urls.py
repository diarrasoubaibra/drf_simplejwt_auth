from django.urls import path
from .views import DashboardView, LoginView, RegisterView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('dashboard/', DashboardView.as_view(), name='Dahboard'),
]