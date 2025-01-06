
from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from employers.models import JobPosting


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    headline = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_images', default='profile_images/blank-profile-picture.png')
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True) 
    city = models.CharField(max_length=100, blank=True, null=True)  
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_website = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('he/him', 'He/Him'), ('she/her', 'She/Her'), ('they/them', 'They/Them')], default='he/him')
    current_position = models.CharField(max_length=255, null=True, blank=True) 
    is_public = models.BooleanField(default=True) 


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    EMPLOYEE_TYPES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ]
    
    LOCATION_TYPES = [
        ('On-site', 'On-site'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),
    ]
    
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    emplyoment_type = models.CharField(max_length=50, choices= EMPLOYEE_TYPES)
    location_type = models.CharField(max_length=50, choices= LOCATION_TYPES)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ('job_seeker_profile', 'company_name', 'role', 'start_date')


class Education(models.Model):
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='educations')
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField(blank=False, null=False)
    end_year = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('job_seeker_profile', 'school_name', 'degree', 'field_of_study')


class Skill(models.Model):
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('job_seeker_profile', 'name')


class Certification(models.Model):
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField(blank=False)
    expiration_date = models.DateField(blank=False)
    
    class Meta:
        unique_together = ('job_seeker_profile', 'name', 'issuing_organization', 'issue_date')




class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Application for {self.job_posting.job_title} by {self.job_seeker.first_name}"

