# Generated by Django 5.1.4 on 2025-01-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobSeekers", "0002_jobapplication"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="resume",
            field=models.FileField(upload_to="resumes/"),
        ),
    ]
