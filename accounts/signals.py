from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from jobSeekers.models import JobSeekerProfile
from employers.models import EmployerProfile
import logging

CustomUser = get_user_model()

@receiver(post_save, sender=CustomUser)
def create_or_update_profile(sender, instance, created, **kwargs):
    try:
        if created:
            # Create profile based on the role
            if instance.role == 'job_seeker':
                JobSeekerProfile.objects.create(
                    user=instance,
                    first_name=instance.first_name or "",
                    last_name=instance.last_name or "",
                    contact_email=instance.email
                )
                logging.info(f"JobSeekerProfile created for user {instance.email}.")
            elif instance.role == 'employer':
                EmployerProfile.objects.create(
                    user=instance,
                    company_name= instance.first_name,
                    contact_email=instance.email
                )
                logging.info(f"EmployerProfile created for user {instance.email}.")
        else:
            # Update profile based on the role
            if instance.role == 'job_seeker':
                profile, _ = JobSeekerProfile.objects.get_or_create(user=instance)
                profile.first_name = instance.first_name or ""
                profile.last_name = instance.last_name or ""
                profile.contact_email = instance.email
                profile.save()
                logging.info(f"JobSeekerProfile updated for user {instance.email}.")
            elif instance.role == 'employer':
                profile, _ = EmployerProfile.objects.get_or_create(user=instance)
                profile.company_name = instance.first_name or "Default Company"
                profile.contact_email = instance.email
                profile.save()
                logging.info(f"EmployerProfile updated for user {instance.email}.")
    except Exception as e:
        logging.error(f"Error creating or updating profile for user {instance.email}: {e}")



# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from profiles.models import JobSeekerProfile
# from employers.models import EmployerProfile

# CustomUser = get_user_model()

# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     print('enter into signals files of accounts ')
#     if created:
        
#         if instance.role == 'jobseeker':
#             JobSeekerProfile.objects.create(user=instance)
#         elif instance.role == 'employer':
#             EmployerProfile.objects.create(user=instance)

