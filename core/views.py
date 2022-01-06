from django.views.generic import TemplateView
from account.models import Profile
from post.models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from .forms import ProfileForm
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'
    paginate_by = 4

    def paginate_queryset(self, queryset, page_size):
        try:
            return super(HomeView, self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(HomeView, self).paginate_queryset(queryset, page_size)


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'core/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user_id = kwargs['pk']
        context['user'] = Profile.objects.get(pk=user_id)
        return context


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'core/profileupdate.html'

    def get_success_url(self):
        pro = Profile.objects.get(user=self.request.user)
        return reverse('profile', kwargs={'pk': pro.id})
