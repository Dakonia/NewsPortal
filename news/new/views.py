from datetime import datetime
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Exists, OuterRef

class PostList(ListView):

    model = Post
    ordering = 'text'
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='author').exists()
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    # def get_cotext_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     context['next_sale'] = None
    #     return context



    def get_queryset(self):
        times = Post.objects.all().order_by('-dateCreation')
        return times


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('new.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.author
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('new.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('new.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['postCategory'] = self.category
        return context



@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)


    message = 'Вы успешно подписались на расылку Новостей категории:'
    return render(request, 'subscribe.html', {'category':category, 'message':message})


@login_required
def not_subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'Вы отписались от подписки на категорию:'
    return render(request, 'subscribe.html', {'category':category, 'message':message})


