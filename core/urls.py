from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('view-posts/', views.view_posts, name='view_posts'),
    path('create/', views.create_post, name='create_post'),
    # path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('toggle-reaction/<int:post_id>/', views.toggle_reaction, name='toggle_reaction'),
    path('post/<int:post_id>/like/', views.toggle_reaction, name='toggle_reaction'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('jobseeker/profile/<int:pk>/', views.jobseeker_profile, name='job_seeker_profile'),
    
]