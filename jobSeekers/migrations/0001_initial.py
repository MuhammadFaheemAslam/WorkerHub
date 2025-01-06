# Generated by Django 5.1.4 on 2025-01-05 20:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JobSeekerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("headline", models.CharField(blank=True, max_length=50, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(
                        default="profile_images/blank-profile-picture.png",
                        upload_to="profile_images",
                    ),
                ),
                ("birthday", models.DateField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contact_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "contact_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("contact_website", models.URLField(blank=True, null=True)),
                ("github_url", models.URLField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("he/him", "He/Him"),
                            ("she/her", "She/Her"),
                            ("they/them", "They/Them"),
                        ],
                        default="he/him",
                        max_length=10,
                    ),
                ),
                (
                    "current_position",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_public", models.BooleanField(default=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school_name", models.CharField(max_length=100)),
                ("degree", models.CharField(max_length=100)),
                ("field_of_study", models.CharField(max_length=100)),
                ("start_year", models.PositiveIntegerField()),
                ("end_year", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "job_seeker_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="jobSeekers.jobseekerprofile",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("job_seeker_profile", "school_name", "degree", "field_of_study")
                },
            },
        ),
        migrations.CreateModel(
            name="Certification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("issuing_organization", models.CharField(max_length=100)),
                ("issue_date", models.DateField()),
                ("expiration_date", models.DateField()),
                (
                    "job_seeker_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certifications",
                        to="jobSeekers.jobseekerprofile",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("job_seeker_profile", "name", "issuing_organization", "issue_date")
                },
            },
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "job_seeker_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="jobSeekers.jobseekerprofile",
                    ),
                ),
            ],
            options={
                "unique_together": {("job_seeker_profile", "name")},
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                (
                    "emplyoment_type",
                    models.CharField(
                        choices=[
                            ("Full-Time", "Full-Time"),
                            ("Part-Time", "Part-Time"),
                            ("Contract", "Contract"),
                            ("Internship", "Internship"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "location_type",
                    models.CharField(
                        choices=[
                            ("On-site", "On-site"),
                            ("Hybrid", "Hybrid"),
                            ("Remote", "Remote"),
                        ],
                        max_length=50,
                    ),
                ),
                ("location", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "job_seeker_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_experiences",
                        to="jobSeekers.jobseekerprofile",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("job_seeker_profile", "company_name", "role", "start_date")
                },
            },
        ),
    ]