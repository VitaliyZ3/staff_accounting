from dataclasses import fields
from re import template
import django_tables2 as tables
from .models import Employer, Status, Insurance, Post


class EmployerTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"class": "id-column", "data-url": 'employer-info'}})

    class Meta:
        model = Employer
        fields = (
            'id',
            'surname',
            'name',
            'patronymic',
            'phone_number',
            'email',
            'status'
        )
        template_name = "django_tables2/bootstrap.html"


class StatusTable(tables.Table):
    class Meta:
        model = Status
        template_name = "django_tables2/bootstrap.html"


class InsuranceTable(tables.Table):
    class Meta:
        model = Insurance
        template_name = "django_tables2/bootstrap.html"


class PostTable(tables.Table):
    class Meta:
        model = Post
        template_name = "django_tables2/bootstrap.html"
