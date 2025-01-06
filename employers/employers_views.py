from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmployerProfile, JobPosting, Follower
from .forms import EmployerProfileForm, JobPostingForm
from jobSeekers.models import JobApplication



@login_required
def view_employer_profile(request):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    context = {'emp_profile': employer_profile}
    return render(request, 'employer/view_profile.html', context)


@login_required
def edit_employer_profile(request):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)

    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, request.FILES, instance=employer_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('view_emp_profile')  
    else:
        form = EmployerProfileForm(instance=employer_profile)

    context = {'form': form,
               'profile':employer_profile}
    return render(request, 'employer/edit_profile.html', context)



#job posting
@login_required
def create_job(request):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.employer = employer_profile
            job_posting.save()
            messages.success(request, "Job created successfully.")
            return redirect('list_jobs')
    else:
        form = JobPostingForm()
        
    context ={
        'form': form,
        'emp_profile':   employer_profile 
    }
    return render(request, 'employer/job_post/job_form.html', context)

@login_required
def edit_job(request, job_id):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    job_posting = get_object_or_404(JobPosting, id=job_id, employer__user=request.user)
    
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job_posting)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully.")
            return redirect('list_jobs')
    else:
        form = JobPostingForm(instance=job_posting)
        
    context ={
        'form': form,
        'emp_profile':   employer_profile 
    }
    
    return render(request, 'employer/job_post/job_form.html', context)


@login_required
def delete_job(request, job_id):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    job_posting = get_object_or_404(JobPosting, id=job_id, employer__user=request.user)
    if request.method == 'POST':
        job_posting.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect('list_jobs')
    
    context ={
        'job_posting': job_posting,
        'emp_profile':   employer_profile 
    }
    return render(request, 'employer/job_post/confirm_delete.html', context)


@login_required
def list_jobs(request):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    jobs = JobPosting.objects.filter(employer=employer_profile)
    
    context ={
        'jobs': jobs,
        'emp_profile':   employer_profile 
    }
    return render(request, 'employer/job_post/job_list.html', context)

    
@login_required
def all_job_listings(request):
    emp_profile = get_object_or_404(EmployerProfile, user=request.user)
    # Fetch all jobs posted across all employers (not filtered by logged-in employer)
    jobs = JobPosting.objects.all()

    context ={
        'jobs': jobs,
        'emp_profile': emp_profile 
    }

    return render(request, 'employer/job_post/all_job_list.html', context)

# function for all other user to see the employer profile

def employers_profile(request, employer_id):
    profile = get_object_or_404(EmployerProfile, user=request.user)
    employers_profile = get_object_or_404(EmployerProfile, pk=employer_id)
    job_postings = JobPosting.objects.filter(employer=employers_profile)
    is_following = employers_profile.followers.filter(id=request.user.id).exists() if request.user.is_authenticated else False

    context = {
        'emp_profile': profile,
        'employers_profile':employers_profile,
        'job_postings': job_postings,
        'is_following': is_following,  # Add is_following to context
    }
    return render(request, 'employer/employer_profile.html', context)

@login_required
def view_applications(request, job_id):
    employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    job_posting = get_object_or_404(JobPosting, pk=job_id, employer__user=request.user)
    applications = JobApplication.objects.filter(job_posting=job_posting)

    context ={
        'job_posting': job_posting, 
        'applications': applications,
        'emp_profile': employer_profile
    }
    return render(request, 'employer/applicants/view_applications.html', context)


@login_required
def follow_employer(request, employer_id):
    # Get the employer profile
    emp_profile = get_object_or_404(EmployerProfile, id=employer_id)
    
    # Ensure the employer can't follow their own profile
    if request.user != emp_profile.user:
        if request.user not in emp_profile.followers.all():
            emp_profile.followers.add(request.user)
    
    # Redirect back to the employer profile page
    return redirect('employers_profile', employer_id=emp_profile.id)

@login_required
def unfollow_employer(request, employer_id):
    # Get the employer profile
    emp_profile = get_object_or_404(EmployerProfile, id=employer_id)
    
    # Ensure the employer can't unfollow their own profile
    if request.user != emp_profile.user:
        if request.user in emp_profile.followers.all(): 
            emp_profile.followers.remove(request.user)

    # Redirect back to the employer profile page
    return redirect('employers_profile', employer_id=emp_profile.id)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_followers(request):
    emp_profile = get_object_or_404(EmployerProfile, user=request.user)
    followers = emp_profile.followers.all()
    
    context = {
        'emp_profile': emp_profile,
        'followers': followers
    }
    
    print(followers)

    return render(request, 'employer/followers_list.html', context)

