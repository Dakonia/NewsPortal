import django_filters
from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateInput, DateTimeInput


class PostFilter(FilterSet):

    class Meta:
       model = Post
       fields = {
           'tittle': ['exact'],
           'categoryType': ['exact'],
           'text':['exact'],
       }

    date = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
