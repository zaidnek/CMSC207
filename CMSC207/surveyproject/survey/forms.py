from django import forms

class QuestionnaireForm(forms.Form):
    # Basic Information
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    staff_name = forms.CharField(label='Name of staff who rendered the service?', max_length=100)
    sex = forms.ChoiceField(label='Sex', choices=(('Male', 'Male'), ('Female', 'Female')), widget=forms.RadioSelect)
    doh_employee = forms.ChoiceField(label='DOH Employee', choices=(('Yes', 'Yes'), ('No', 'No')), widget=forms.RadioSelect)
    team_acronym = forms.CharField(label='Team (Acronym)', max_length=20)
    bureau_service_region_acronym = forms.CharField(label='Bureau/Service/Region (Acronym):', max_length=50)
    activity_name = forms.CharField(label='Name of Activity', max_length=100)
    
    # Section A: Overall Expectation
    EXPECTATION_CHOICES = [
        ('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Very Good'), ('6', 'Excellent'), ('7', 'Outstanding')
    ]
    expectation = forms.ChoiceField(label='Section A: How would you rate your overall expectation of the service provider’s service?', choices=EXPECTATION_CHOICES, widget=forms.RadioSelect)

    # Section B: Statement Ratings fields...
    STATEMENTS = {
        "The service provider/s provides its service at the time it promises to do so.": 'statement1',
        "You receive prompt service from service providers.": 'statement2',
        "The service provider/s is/are polite.": 'statement3',
        "The service provider/s is/are sensitive to the client’s needs.": 'statement4',
        "The service provider/s is/are well dressed and appear neat.": 'statement5',
        "The appearance of the physical/virtual facility of the service provider is in keeping with the type of service/s provided.": 'statement6'
    }
    for statement, field_name in STATEMENTS.items():
        locals()[field_name] = forms.ChoiceField(
            label=statement,  # Set label for each statement
            choices=[(i, i) for i in range(1, 8)],
            widget=forms.RadioSelect
        )

    # Section C: Service Quality
    QUALITY_CHOICES = [
        ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Excellent')
    ]
    quality = forms.ChoiceField(label='Section C: Overall, how would you rate the quality of service provided by the service provider/s?', choices=QUALITY_CHOICES, widget=forms.RadioSelect)

    # Section D: Comments and Feedback
    # comments = forms.CharField(label='Section D: For comments, recommendations, concerns, or aspects of our service(s) that need improvement, please put it down below. If you wish for us to respond to your feedback, please include your contact details.', widget=forms.Textarea)
    comments = forms.CharField(
        label='Section D: For comments, recommendations, concerns, or aspects of our service(s) that need improvement, please put it down below. If you wish for us to respond to your feedback, please include your contact details.',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 100})  # Adjust the rows and cols as needed
    )


    def clean(self):
        cleaned_data = super().clean()

        # Perform custom validation here
        # Example: Ensure that either 'Male' or 'Female' is selected for the 'sex' field
        sex = cleaned_data.get('sex')
        if sex not in ['Male', 'Female']:
            self.add_error('sex', 'Please select a valid option for sex.')

        # Add more custom validation rules as needed...

        return cleaned_data

