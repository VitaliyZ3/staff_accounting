from dataclasses import field
import django_filters
from .models import Employer, Insurance, Status, Post

class EmployerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Employer
        fields = ('id', 'surname', 'name', 'patronymic', 'phone_number', 'email')


class InsuranceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Insurance
        fields = '__all__'


class StatusFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Status
        fields = '__all__'


class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Post
        fields = '__all__'