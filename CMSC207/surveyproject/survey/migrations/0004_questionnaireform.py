# Generated by Django 5.0.3 on 2024-03-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_remove_userresponse_response_question_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('staff_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('doh_employee', models.CharField(max_length=10)),
                ('expectation', models.CharField(max_length=20)),
                ('statement1', models.IntegerField()),
                ('statement2', models.IntegerField()),
                ('statement3', models.IntegerField()),
                ('statement4', models.IntegerField()),
                ('statement5', models.IntegerField()),
                ('statement6', models.IntegerField()),
                ('quality', models.CharField(max_length=10)),
                ('comments', models.TextField()),
            ],
        ),
    ]
