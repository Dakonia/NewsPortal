from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail
from .models import Post


urlpatterns = [
         path('<int:pk>', PostDetail.as_view()),
         path('', PostList.as_view())
]

