from django import forms
from .models import Job, JobApplication
from .models import User

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description", "required_skills", "employer", "location", 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["employer"].queryset = User.objects.filter(role="employer")

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["cover_letter"]