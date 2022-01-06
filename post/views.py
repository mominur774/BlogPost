from .models import Post
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, FormView):
    template_name = 'post/create.html'
    form_class = PostCreateForm
    success_url = '/dashboard/'
    success_message = 'Post created!'

    def form_valid(self, form):
        user = self.request.user
        title = form.cleaned_data['title']
        desc = form.cleaned_data['description']
        Post(user=user, title=title, description=desc).save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/update.html'
    success_url = '/dashboard/'
    success_message = 'Post updated!'


@method_decorator(login_required, name='dispatch')
class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')
    success_message = 'Post deleted!'
