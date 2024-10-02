from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_ls, name='job_ls'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
]
