from django.urls import path
from .views import upgrade_user


urlpatterns = [
    path('upgrade/', upgrade_user, name='account_upgrade'),
]