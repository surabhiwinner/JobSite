from django.urls import path

from . import views


urlpatterns = [
    path('home/',views.HomeView.as_view(), name = 'home'),
    path('joblist/', views.JobListView.as_view(), name='joblist'),
    path('employers-job-list/',views.EmployersJobView.as_view(), name='employers'),
    # path('create-jobs/', views.CreateEmployerJobsView.as_view(),name ='create-jobs'),
    path('job-details/<str:uuid>/', views.JobDetailView.as_view(), name='jobdetails'),
    # path('job-employer-delete/<str:uuid>/', views.JobEmployerDeleteView.as_view(), name= 'job-employer-delete'),
    # path('job-employer-update/<str:uuid>/', views.EmployerJobUpdateView.as_view(), name='employer-update-job'),
    path('create-job/', views.CreateJobView.as_view(), name='create-job'),
]