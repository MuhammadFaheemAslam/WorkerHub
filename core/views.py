from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from jobSeekers.models import JobSeekerProfile
from employers.models import EmployerProfile
from django.contrib import messages
from .models import Post, PostMedia, PostReaction, Comment
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from accounts.models import CustomUser
from jobSeekers.models import JobPosting


    
def welcome(request):
    return render(request, 'core/welcome.html')


@login_required
def home(request):
    posts = view_posts(request)
    create_post(request) 

    for post in posts:
        post.has_reacted = post.reactions.filter(user=request.user).exists()
        post.has_liked = post.reactions.filter(user=request.user, is_like=True).exists()

    if request.user.role == 'job_seeker':
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
        context = {
            'profile': profile,
            'posts': posts,
        }
        return render(request, 'core/home.html', context)
    
    elif request.user.role == 'employer':
        profile = get_object_or_404(EmployerProfile, user=request.user)
        context = {
            'emp_profile': profile,
            'posts': posts,
        }
        return render(request, 'core/home.html', context)


@login_required
def view_posts(request):
    posts = Post.objects.all().order_by('-created_at')

    for post in posts:
        # Check if the post's user has a JobSeekerProfile or EmployerProfile
        if hasattr(post.user, 'jobseekerprofile'):
            post.profile = post.user.jobseekerprofile
            post.profile_type = 'job_seeker'
        elif hasattr(post.user, 'employerprofile'):
            post.profile = post.user.employerprofile
            post.profile_type = 'employer'
        else:
            post.profile = None
            post.profile_type = None

        # Add media details if the post has media
        for media in post.media.all():
            media.file_extension = media.file.name.split('.')[-1]

    context = {
        'posts': posts,
    }

    return posts


def handle_uploaded_files(post, files, media_type):
    """Helper function to handle media uploads."""
    for file in files:
        PostMedia.objects.create(post=post, media_type=media_type, file=file)

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')
        media_files = request.FILES.getlist('mediaFile')
        post = Post.objects.create(user=request.user, content=content)

        handle_uploaded_files(post, images, 'image')
        handle_uploaded_files(post, videos, 'video')
        handle_uploaded_files(post, media_files, 'document')

        messages.success(request, 'Your post has been created successfully!')
        return redirect('home') 
    
    

@login_required
def delete_post(request, post_id):    
    if request.user.role == 'job_seeker':
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
    else:
        profile = get_object_or_404(EmployerProfile, user=request.user)
    
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')  
    context = {
        'post': post,
        'profile': profile,
        'emp_profile': profile
        }
    return render(request, 'posts/delete_post.html', context)

@login_required
def toggle_reaction(request, post_id):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        existing_reaction = PostReaction.objects.filter(user=user, post=post).first()

        if existing_reaction:
            existing_reaction.is_like = not existing_reaction.is_like  
            existing_reaction.save()
        else:
            existing_reaction = PostReaction.objects.create(user=user, post=post, is_like=True)

        return JsonResponse({
            'is_like': existing_reaction.is_like
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)



@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')
        parent_comment = request.POST.get('parent_comment') 
        
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            content=content,
            parent_comment=None if parent_comment == "" else Comment.objects.get(id=parent_comment)
        )
        return redirect('post_detail', post_id=post.id)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post, parent_comment=None).order_by('-created_at')
    all_comments = Comment.objects.filter(post=post).order_by('created_at')
    
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'all_comments': all_comments,
    })



@login_required
def jobseeker_profile(request, pk):
    
    if request.user.role == 'job_seeker': 
        profile = get_object_or_404(JobSeekerProfile, user=request.user)   
        
        post_user_profile = get_object_or_404(JobSeekerProfile, pk=pk)
        work_experiences = post_user_profile.work_experiences.all().order_by('-start_date')
        educations = post_user_profile.educations.all().order_by('-start_year')
        skills = post_user_profile.skills.all()
        certifications = post_user_profile.certifications.all().order_by('-issue_date')

        context = {
            'profile': profile,
            'post_user_profile': post_user_profile,
            'work_experiences': work_experiences,
            'educations': educations,
            'skills': skills,
            'certifications': certifications,
        }

    elif request.user.role == 'employer':
        emp_profile = get_object_or_404(EmployerProfile, user=request.user)
        
        post_user_profile = get_object_or_404(JobSeekerProfile, pk=pk)
        work_experiences = post_user_profile.work_experiences.all().order_by('-start_date')
        educations = post_user_profile.educations.all().order_by('-start_year')
        skills = post_user_profile.skills.all()
        certifications = post_user_profile.certifications.all().order_by('-issue_date')

        context = {
            'emp_profile':emp_profile,
            'post_user_profile': post_user_profile,
            'work_experiences': work_experiences,
            'educations': educations,
            'skills': skills,
            'certifications': certifications,
        }
        
    return render(request, 'core/view_jobSeekers_profile.html', context)
    
    

@login_required
def employers_profile(request, employer_id):
    if request.user.role == 'job_seeker': 
        profile = get_object_or_404(JobSeekerProfile, user=request.user)   
        employers_profile = get_object_or_404(EmployerProfile, pk=employer_id)
        job_postings = JobPosting.objects.filter(employer=employers_profile)
        is_following = employers_profile.followers.filter(id=request.user.id).exists() if request.user.is_authenticated else False

        context = {
            'profile': profile,
            'employers_profile': employers_profile,
            'job_postings': job_postings,
            'is_following': is_following, 
        }
    
    elif request.user.role == 'employer':
        profile = get_object_or_404(EmployerProfile, user=request.user)
        employers_profile = get_object_or_404(EmployerProfile, pk=employer_id)
        job_postings = JobPosting.objects.filter(employer=employers_profile)
        is_following = employers_profile.followers.filter(id=request.user.id).exists() if request.user.is_authenticated else False

        context = {
            'emp_profile': profile,
            'employers_profile':employers_profile,
            'job_postings': job_postings,
            'is_following': is_following,  
        }
        
    return render(request, 'core/view_employers_profile.html', context)