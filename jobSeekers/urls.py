from django.urls import path
from . import jobSeekers_views as views 
urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('view/', views.view_profile, name='view_profile'),
#work experience
    path('add-work-experience/', views.add_work_experience, name='add_work_experience'),
    path('edit-work-experience/', views.edit_allwork_experience, name='edit_allwork_experience'),
    path('edit-work-experience/<int:pk>/', views.edit_work_experience, name='edit_work_experience'),
    path('delete-work-experience/<int:pk>/', views.delete_work_experience, name='delete_work_experience'),
    
 # Education
    path('add-education/', views.add_education, name='add_education'),
    path('edit-education/', views.edit_alleducation, name='edit_alleducation'),
    path('edit-education/<int:pk>/', views.edit_education, name='edit_education'),
    path('delete-education/<int:pk>/', views.delete_education, name='delete_education'),
# Skills
    path('add-skill/', views.add_skill, name='add_skill'), 
    path('edit-skill/', views.edit_allskills, name='edit_allskills'),
    path('edit-skill/<int:pk>/', views.edit_skill, name='edit_skill'),
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete_skill'),
# Certifications   
    path('add-certification/', views.add_certification, name='add_certification'),
     path('edit-certification/', views.edit_allcertifications, name='edit_allcertifications'),
    path('edit-certification/<int:pk>/', views.edit_certification, name='edit_certification'),
    path('delete-certification/<int:pk>/', views.delete_certification, name='delete_certification'),
#contact info 
    # path('contact-info/',views.contact_info, name='contact_info'),
    path('edit-contact-info/', views.edit_contact_info, name='edit_contact_info'), 
#jobs details & apply
    path('jobs/', views.job_listing, name='job_listing'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'), 
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    
    path('employer/<int:employer_id>/follow/', views.follow_employers, name='follow_employers'),
    path('employer/<int:employer_id>/unfollow/', views.unfollow_employers, name='unfollow_employers'),
]
