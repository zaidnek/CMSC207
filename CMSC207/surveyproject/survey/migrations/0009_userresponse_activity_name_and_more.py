# Generated by Django 5.0.3 on 2024-03-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_userresponse_comments_userresponse_expectation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='activity_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='bureau_service_region_acronym',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='doh_employee',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='staff_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='team_acronym',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
