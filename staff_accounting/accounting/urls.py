from django.urls import path
#views
from .views import (
    EmployerListView, InsuranceListView, StatusListView, PostListView
)

urlpatterns = [
    path('', EmployerListView.as_view(), name='employer-table'),
    path('insuranse-table/', InsuranceListView.as_view(), name='insurance-table'),
    path('status-table/', StatusListView.as_view(), name='status-table'),
    path('post-table/', PostListView.as_view(), name='post-table'),
]   
