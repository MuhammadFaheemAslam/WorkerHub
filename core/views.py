from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from jobSeekers.models import JobSeekerProfile
from employers.models import EmployerProfile
from django.contrib import messages

@login_required
def home(request):

    if request.user.role == 'job_seeker':
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
        context ={
            'profile':profile
        }
        return render(request, 'core/home.html', context)
    
    elif request.user.role == 'employer':
        profile = get_object_or_404(EmployerProfile, user=request.user)
        
        context ={
            'emp_profile':profile
        }
    
        return render(request, 'core/employer/home.html', context)

        # return redirect('login')
    
    


def welcome(request):
    return render(request, 'core/welcome.html')
