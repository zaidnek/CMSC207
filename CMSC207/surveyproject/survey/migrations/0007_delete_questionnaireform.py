# Generated by Django 5.0.3 on 2024-03-25 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_userresponse_choice_userresponse_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionnaireForm',
        ),
    ]
