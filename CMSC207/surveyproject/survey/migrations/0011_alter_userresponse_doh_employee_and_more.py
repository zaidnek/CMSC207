# Generated by Django 5.0.3 on 2024-03-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_userresponse_statement_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='doh_employee',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
