from django.urls import path
# views
from .views import (
    EmployerListView, InsuranceListView, StatusListView, PostListView,
    EmployerCreateView, InsuranceCreateView, StatusCreateView, PostCreateView, EmployerInfo
)

urlpatterns = [
    # main page
    path('', EmployerListView.as_view(), name='employer-table'),

    # employer info
    path('employer-info/<int:pk>/', EmployerInfo.as_view(), name='employer-info'),

    # table view
    path('insuranse-table/', InsuranceListView.as_view(), name='insurance-table'),
    path('status-table/', StatusListView.as_view(), name='status-table'),
    path('post-table/', PostListView.as_view(), name='post-table'),

    # create view
    path('employer-create/', EmployerCreateView.as_view(), name='employer-create'),
    path('insuranse-create/', InsuranceCreateView.as_view(),
         name='insurance-create'),
    path('status-create/', StatusCreateView.as_view(), name='status-create'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),

]
