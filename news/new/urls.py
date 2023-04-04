from django.urls import path
# Импортируем созданное нами представление
from .views import (PostList, PostDetail, NewsSearch, PostCreate, PostUpdate, PostDelete)
from .models import Post
from .filters import PostFilter

urlpatterns = [
         path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
         path('', PostList.as_view(), name = 'post_list'),
         path('search', NewsSearch.as_view(), name = 'post_search'),
         path('create/', PostCreate.as_view(), name = 'post_create'),
         path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
         path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]

