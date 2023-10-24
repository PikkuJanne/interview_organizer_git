from django import forms
from django.forms.widgets import DateTimeInput, Textarea
from .models import Interview

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [
            'headline', 
            'datetime', 
            'place', 
            'interviewees', 
            'contact_persons',
            'contact_emails',
            'contact_phones',
            'notes',
            'links',
            'questions',
        ]
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'interviewees': Textarea(attrs={'rows': 3, 'style': 'width: 55%;'}),
            'contact_persons': Textarea(attrs={'rows': 3, 'style': 'width: 55%;'}),
            'contact_emails': Textarea(attrs={'rows': 3, 'style': 'width: 55%;'}),
            'contact_phones': Textarea(attrs={'rows': 3, 'style': 'width: 55%;'}),
            'notes': Textarea(attrs={'rows': 4, 'style': 'width: 100%;'}),
            'links': Textarea(attrs={'rows': 4, 'style': 'width: 100%;'}),
            'questions': Textarea(attrs={'rows': 10, 'style': 'width: 100%;'}),
        }

class NewInterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['headline', 'datetime', 'place']
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }