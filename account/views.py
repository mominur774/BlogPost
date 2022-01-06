from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import RedirectView
from .forms import SignUpForm, LoginForm, ResetConfirmForm, ResetForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = '/login/'
    success_message = 'Account created successfully!'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        self.request.session['username'] = username
        return super().form_valid(form)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_message = 'User logged in successfully!'


@method_decorator(login_required, name='dispatch')
class UserLogoutView(RedirectView):
    url = '/login/'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UserPasswordChange(PasswordChangeView):
    template_name = 'account/changepass.html'
    form_class = UserPasswordChangeForm


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/resetpass.html'
    form_class = ResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/resetconfirm.html'
    form_class = ResetConfirmForm
