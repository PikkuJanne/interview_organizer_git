from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    """Interview the user is planning."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Updated this line
    headline = models.CharField(max_length=200)
    datetime = models.DateTimeField()  # Combined date and time field
    place = models.CharField(max_length=200, blank=True)
    interviewees = models.TextField(blank=True, help_text='Separate multiple interviewees with line breaks.')
    contact_persons = models.TextField(blank=True, help_text='Separate multiple persons with line breaks.')
    contact_emails = models.TextField(blank=True, help_text='Separate multiple emails with line breaks.')
    contact_phones = models.TextField(blank=True, help_text='Separate multiple phone numbers with line breaks.')
    notes = models.TextField(blank=True, help_text='Separate multiple notes with line breaks.')
    links = models.TextField(blank=True, help_text='Separate multiple links with line breaks.')
    questions = models.TextField(blank=True, help_text='Separate multiple questions with line breaks.')
    date_added = models.DateTimeField(auto_now_add=True, help_text='Separate lines with line breaks.')

    def __str__(self):
        """Return string representation of model."""
        return self.headline

    def is_upcoming(self):
        """Return True if interview is upcoming, False if it's in the past."""
        from datetime import datetime
        return self.datetime > datetime.now()
