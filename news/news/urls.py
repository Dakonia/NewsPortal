from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
  # path('post/', include('new.urls')),
   path('news/', include('new.urls'))
]