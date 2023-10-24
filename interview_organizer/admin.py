from django.contrib import admin
from django import forms
from .models import Interview

class InterviewAdmin(admin.ModelAdmin):
    inlines = []

# Register the models with the admin site
admin.site.register(Interview, InterviewAdmin)

