from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.timezone import now
from django.conf import settings


CustomUser = get_user_model()  # Custom user model

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_images', default='company_images/company_logos/blank-pic.png')
    company_pictures = models.ImageField(upload_to='company_images', default='company_images/blank-pic.png')
    company_description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_website = models.URLField(blank=True, null=True)
    company_created_date = models.DateTimeField(auto_now_add=True)

    # Many-to-many relationship to CustomUser (followers)
    followers = models.ManyToManyField(CustomUser, related_name='following_employer', blank=True)

    def __str__(self):
        return self.company_name

    def get_followers_count(self):
        return self.followers.count()

    def get_jobs_posted(self):
        return self.job_postings.all()


class Follower(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='follower_employer')  # Changed related_name here
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['employer', 'user']  # Prevents duplicate follow entries.

    def __str__(self):
        return f"{self.user.username} follows {self.employer.company_name}"
    


class JobPosting(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('', 'Select Experience Level'),
        ('Entry', 'Entry Level'),
        ('Mid', 'Mid Level'),
        ('Senior', 'Senior Level'),
    ]
    JOB_TYPE_CHOICES = [
        ('', 'Select job type'),
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
    ]
    LOCATION_TYPE_CHOICES = [
        ('', 'Select Location type'),
        ('On-Site', 'On-Site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]
    
    employer = models.ForeignKey( 'employers.EmployerProfile',on_delete=models.CASCADE,related_name='job_postings')
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    location_type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES)
    application_deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']
        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title

    def is_expired(self):
        """Check if the job posting has expired."""
        if self.application_deadline:
            return now().date() > self.application_deadline
        return False

    def formatted_salary(self):
        """Format salary range for display."""
        if self.salary_min and self.salary_max:
            return f"${self.salary_min} - ${self.salary_max}"
        elif self.salary_min:
            return f"From ${self.salary_min}"
        elif self.salary_max:
            return f"Up to ${self.salary_max}"
        return "Not specified"



class Employee(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='employees')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    joined_on = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, blank=True, null=True)  # Optional field for role/title

    def __str__(self):
        return f"{self.user.username} works at {self.employer.company_name}"


