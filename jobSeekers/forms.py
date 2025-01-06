from django import forms
from .models import JobSeekerProfile, WorkExperience, Education, Skill, Certification, JobApplication


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['first_name', 'last_name', 'headline', 'bio', 'profile_picture', 'birthday', 'location', 'country', 'city', 'postal_code', 'contact_email', 'contact_phone', 'contact_website', 'github_url', 'gender', 'current_position', 'is_public']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'headline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Headline'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell us about yourself...'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Phone'}),
            'contact_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'GitHub URL'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'current_position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Position'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company_name', 'role', 'emplyoment_type', 'location_type', 'location', 'start_date', 'end_date', 'description']
        
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'emplyoment_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Employment Type'}),
            'location_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Location Type'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job Description'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'field_of_study', 'start_year', 'end_year']
        
        widgets = {
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter degree'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field of study'}),
            'start_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Start year', 'min': 1900, 'max': 2100}),
            'end_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'End year', 'min': 1900, 'max': 2100}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter skill name'}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuing_organization', 'issue_date', 'expiration_date']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter certification name'}),
            'issuing_organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter issuing organization'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }




class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']  # Fields that the job seeker can fill
        widgets = {
            'resume': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx'  # You can restrict file types here
            }),
            'cover_letter': forms.Textarea(attrs={
                'placeholder': 'Write a brief cover letter...',
                'class': 'form-control',
                'rows': 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        self.fields['resume'].required = True  
