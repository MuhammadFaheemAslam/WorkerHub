from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

ROLE_CHOICES = [
    ('job_seeker', 'Job Seeker'),
    ('employer', 'Employer'),
]

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Role"
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'role']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("An account already exists with this email address.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if role == 'job_seeker':
            if not first_name:
                self.add_error('first_name', "First name is required for job seekers.")
            if not last_name:
                self.add_error('last_name', "Last name is required for job seekers.")
        elif role == 'employer':
            if not first_name:
                self.add_error('first_name', "first name is required for employers.")

        return cleaned_data

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        if not re.search(r'[a-z]', password):
            raise ValidationError('Password must contain at least one lowercase letter.')
        if not re.search(r'\d', password):
            raise ValidationError('Password must contain at least one number.')
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError('Password must contain at least one special character (@$!%*?&).')
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Use email as the username
        if commit:
            user.save()
        return user
