from django import forms
from .models import EmployerProfile, JobPosting, Follower, Employee
from django.contrib.auth import get_user_model

CustomUser = get_user_model()  # Assuming you are using a custom user model

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name', 'company_logo','company_pictures', 'company_description', 'location', 'contact_email', 'contact_phone', 'contact_website'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter company name', 'class': 'form-control'}),
            'company_logo': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'company_pictures': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'company_description': forms.Textarea(attrs={ 'rows': 5,'placeholder': 'Write a brief description of your company...','class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'City, Country', 'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'placeholder': 'example@company.com', 'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'placeholder': 'Contact number (e.g. +1234567890)', 'class': 'form-control'}),
            'contact_website': forms.URLInput(attrs={'placeholder': 'Website-url', 'class': 'form-control'}),
        }


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['job_title', 'job_description', 'job_location', 'location_type', 'job_type', 'salary_min', 'salary_max', 'experience_level', 'application_deadline']
        widgets = {
            'job_title': forms.TextInput(attrs={'placeholder': 'Job title (e.g. Software Engineer)', 'class': 'form-control'}),
            'job_description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter detailed job description...', 'class': 'form-control'}),
            'job_location': forms.TextInput(attrs={'placeholder': 'Location (e.g. New York, USA)', 'class': 'form-control'}),
            'location_type': forms.Select(attrs={'class': 'form-select'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'salary_min': forms.NumberInput(attrs={'placeholder': 'Minimum salary (e.g. 50000)', 'class': 'form-control'}),
            'salary_max': forms.NumberInput(attrs={'placeholder': 'Maximum salary (e.g. 80000)', 'class': 'form-control'}),
            'experience_level': forms.Select(attrs={'class': 'form-select'}),
            'application_deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }



# Form for adding/removing followers
class FollowerForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ['user']  # Allow the employer to add users as followers
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
        }

# Form for adding/removing employees
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'role']  # Allow the employer to add users as employees with a role
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.TextInput(attrs={'placeholder': 'Employee role (e.g. Developer)', 'class': 'form-control'}),
        }
