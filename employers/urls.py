from django.urls import path
from . import employers_views as views

urlpatterns = [
    path('emp_edit/', views.edit_employer_profile, name='edit_emp_profile'),
    path('emp_view/', views.view_employer_profile, name='view_emp_profile'),
    path('jobs/', views.list_jobs, name='list_jobs'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('jobs/<int:job_id>/applications/', views.view_applications, name='view_applications'),
    path('profile/<int:employer_id>/', views.employer_profile, name='employer_profile'),
    path('employer/<int:employer_id>/follow/', views.follow_employer, name='follow_employer'),
    path('employer/<int:employer_id>/unfollow/', views.unfollow_employer, name='unfollow_employer'),


]