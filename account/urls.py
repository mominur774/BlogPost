from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('changepass/', views.UserPasswordChange.as_view(), name="changepass"),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='account/changedone.html'),
         name="password_change_done"),
    path('password_reset/', views.UserPasswordResetView.as_view(),
         name="password_reset"),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name="account/resetdone.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='account/complete.html'),
         name="password_reset_complete")
]
