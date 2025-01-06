# Generated by Django 5.1.4 on 2025-01-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employers", "0002_alter_jobposting_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobposting",
            name="experience_level",
            field=models.CharField(
                choices=[
                    ("", "Select Experience Level"),
                    ("Entry", "Entry Level"),
                    ("Mid", "Mid Level"),
                    ("Senior", "Senior Level"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="jobposting",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("", "Select job type"),
                    ("Full-Time", "Full-Time"),
                    ("Part-Time", "Part-Time"),
                    ("Contract", "Contract"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="jobposting",
            name="location_type",
            field=models.CharField(
                choices=[
                    ("", "Select Location type"),
                    ("On-Site", "On-Site"),
                    ("Remote", "Remote"),
                    ("Hybrid", "Hybrid"),
                ],
                max_length=50,
            ),
        ),
    ]
