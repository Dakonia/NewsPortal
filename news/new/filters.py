import django_filters
from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateInput, DateTimeInput

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):

    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'tittle': ['exact'],
           'categoryType': ['exact'],
           'dateCreation': ['exact'],
           # количество товаров должно быть больше или равно # цена должна быть больше или равна указанной
       }

    date = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Date',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )

    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label= 'Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )