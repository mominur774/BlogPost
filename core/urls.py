from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name="profile"),
    path('profileupdate/<int:pk>/',
         views.ProfileUpdateView.as_view(), name="profileupdate"),
]
