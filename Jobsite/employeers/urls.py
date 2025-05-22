from django.urls import path

from . import views



urlpatterns = [

    path('employeers-list/', views.EmployeersListView.as_view(), name='employeers-list'),
    path('employer-detail/<str:uuid>/', views.EmployersDetailView.as_view(), name='employer-detail'),
    path('employer-jobs/<str:uuid>/', views.EmployerJobView.as_view(), name='employer-jobs')
]