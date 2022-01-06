from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name="create"),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="delete"),
]
