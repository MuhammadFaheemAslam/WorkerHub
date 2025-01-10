# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from jobSeekers.models import JobSeekerProfile
# from employers.models import EmployerProfile
# from django.contrib import messages
# from posts.models import Post, PostMedia
# from posts.posts_views import create_post, view_posts

# # from .forms import CommentForm  
# @login_required
# def home(request):
#     posts, comment_form = view_posts(request)
#     create_post(request) 

#     for post in posts:
#         post.has_reacted = post.reactions.filter(user=request.user).exists()

#     # Logic based on user role
#     if request.user.role == 'job_seeker':
#         profile = get_object_or_404(JobSeekerProfile, user=request.user)
#         context = {
#             'profile': profile,
#             'posts': posts,
#             'comment_form': comment_form
#         }
#         return render(request, 'core/home.html', context)
    
#     elif request.user.role == 'employer':
#         profile = get_object_or_404(EmployerProfile, user=request.user)
#         context = {
#             'emp_profile': profile,
#             'posts': posts,
#         }
#         return render(request, 'core/employer/home.html', context)
    
    
# def welcome(request):
#     return render(request, 'core/welcome.html')

