from datetime import datetime
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import Post
from django.utils import timezone
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

class PostList(ListView):

    model = Post
    ordering = 'text'
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
      #  context['filterset'] = self.filterset
       # return context

    #def get_queryset(self):
     #   queryset = super().get_queryset()
      #  self.filterset = PostFilter(self.request.GET, queryset)
       # return self.filterset.qs


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
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'



class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
