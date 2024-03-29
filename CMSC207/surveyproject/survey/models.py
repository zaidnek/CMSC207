from django.db import models
from django.contrib.auth.models import User
from django import forms

# class Survey(models.Model):
#     title = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     TEXT = 'text'
#     CHOICE = 'choice'
#     LIKERT = 'likert'
#     QUESTION_TYPES = [
#         (TEXT, 'Text'),
#         (CHOICE, 'Choice'),
#         (LIKERT, 'Likert Scale'),
#     ]
    
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
#     text = models.TextField(null=True)
#     type = models.CharField(max_length=10, choices=QUESTION_TYPES, default=TEXT, null=True)

#     def __str__(self):
#         return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
#     text = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.text

# class AnswerOption(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
#     text = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.text

class UserResponse(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    # choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    # answer = models.CharField(max_length=100, null=True)

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    staff_name = models.CharField(max_length=100, null=True)
       
    SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, null=True)
    
    DOH_EMPLOYEE_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ]
    doh_employee = models.CharField(max_length=3, choices=DOH_EMPLOYEE_CHOICES, null=True)

    team_acronym = models.CharField(max_length=20, null=True)
    bureau_service_region_acronym = models.CharField(max_length=50, null=True)
    activity_name = models.CharField(max_length=100, null=True)
    expectation = models.CharField(max_length=20, null=True)
    statement1_rating = models.IntegerField(null=True)
    statement2_rating = models.IntegerField(null=True)
    statement3_rating = models.IntegerField(null=True)
    statement4_rating = models.IntegerField(null=True)
    statement5_rating = models.IntegerField(null=True)
    statement6_rating = models.IntegerField(null=True)
    quality = models.CharField(max_length=20, null=True)
    comments = models.TextField(null=True)


    def __str__(self):
        return f"UserResponse object (id: {self.id})"


class QuestionnaireForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    date = forms.DateField(label='Date')
    staff_name = forms.CharField(max_length=100, label='Name of staff who rendered the service?')
    sex = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect, label='Sex')
    doh_employee = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect, label='DOH Employee')
    team_acronym = forms.CharField(max_length=20, label='Team (Acronym)')
    bureau_service_region_acronym = forms.CharField(max_length=50, label='Bureau/Service/Region (Acronym)')
    activity_name = forms.CharField(max_length=100, label='Name of Activity')
    
    EXPECTATION_CHOICES = [
        ('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Very Good'), ('6', 'Excellent'), ('7', 'Outstanding')
    ]
    expectation = forms.ChoiceField(choices=EXPECTATION_CHOICES, widget=forms.RadioSelect, label='Section A: How would you rate your overall expectation of the service provider’s service?')

    STATEMENTS = {
        "The service provider/s provides its service at the time it promises to do so.": 'statement1',
        "You receive prompt service from service providers.": 'statement2',
        "The service provider/s is/are polite.": 'statement3',
        "The service provider/s is/are sensitive to the client’s needs.": 'statement4',
        "The service provider/s is/are well dressed and appear neat.": 'statement5',
        "The appearance of the physical/virtual facility of the service provider is in keeping with the type of service/s provided.": 'statement6'
    }
    statement_ratings = forms.ChoiceField(choices=[(i, i) for i in range(1, 8)], widget=forms.RadioSelect, label='Section B: Please show the extent to which you think the service provider and their office (if applicable) possess the features described by each statement below:')

    QUALITY_CHOICES = [
        ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Excellent')
    ]
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, widget=forms.RadioSelect, label='Section C: Overall, how would you rate the quality of service provided by the service provider/s?')

    comments = forms.CharField(widget=forms.Textarea, label='Section D: For comments, recommendations, concerns, or aspects of our service(s) that need improvement, please put it down below. If you wish for us to respond to your feedback, please include your contact details.')