from django.shortcuts import render
# import project modules
from .models import Employer, Status, Insurance, Post
from .tables import EmployerTable, StatusTable, InsuranceTable, PostTable
from .filters import EmployerFilter, StatusFilter, InsuranceFilter, PostFilter
# downloaded fraemworks
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView


# table views
class EmployerListView(SingleTableMixin, FilterView):
    model = Employer
    table_class = EmployerTable
    filterset_class = EmployerFilter

    template_name = 'accounting/employer_table_list.html'

class StatusListView(SingleTableMixin, FilterView):
    model = Status
    table_class = StatusTable
    filterset_class = StatusFilter

    template_name = 'accounting/status_table_list.html'

class InsuranceListView(SingleTableMixin, FilterView):
    model = Insurance
    table_class = InsuranceTable
    filterset_class = InsuranceFilter

    template_name = 'accounting/insurance_table_list.html'

class PostListView(SingleTableMixin, FilterView):
    model = Post
    table_class = PostTable
    filterset_class = PostFilter

    template_name = 'accounting/post_table_list.html'


