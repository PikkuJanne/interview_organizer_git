from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Interview
from .forms import InterviewForm, NewInterviewForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden

def index(request):
    """Homepage of Interview Organizer."""
    # If the user is authenticated, they can see more content.
    if request.user.is_authenticated:
        return render(request, 'index.html')
    # If the user is not authenticated, they see only the introductory text.
    else:
        return render(request, 'index_public.html')

@login_required
def upcoming(request):
    """Page that shows upcoming interviews."""
    current_datetime = timezone.now()
    upcoming_interviews = Interview.objects.filter(datetime__gt=current_datetime, owner=request.user).order_by('datetime')
    context = {'upcoming_interviews': upcoming_interviews}
    return render(request, 'upcoming.html', context)

@login_required
def archive(request):
    """Page that shows archived interviews."""
    current_datetime = timezone.now()
    archived_interviews = Interview.objects.filter(datetime__lt=current_datetime, owner=request.user).order_by('-datetime')
    context = {'archived_interviews': archived_interviews}
    return render(request, 'archive.html', context)

@login_required
def interview(request, interview_id):
    """Page that shows single interview."""
    interview = get_object_or_404(Interview, id=interview_id, owner=request.user)
    interviewees = interview.interviewees.split('\n') 
    contact_persons = interview.contact_persons.split('\n')
    contact_emails = interview.contact_emails.split('\n')
    contact_phones = interview.contact_phones.split('\n')
    notes = interview.notes.split('\n')
    links = interview.links.split('\n')
    questions = interview.questions.split('\n')
    context = {
        'interview': interview,
        'interviewees': interviewees,
        'contact_persons': contact_persons,
        'emails': contact_emails,
        'phone_numbers': contact_phones,
        'notes': notes,
        'links': links,
        'questions': questions,
    }
    return render(request, 'interview.html', context)

@login_required
def questions(request, interview_id):
    """Page that shows questions for single interview."""
    interview = get_object_or_404(Interview, id=interview_id, owner=request.user)
    questions = interview.questions.split('\n')
    context = {
        'interview': interview,
        'questions': questions,
    }
    return render(request, 'questions.html', context)

@login_required
def new_interview(request):
    """Page for adding new interview."""
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            new_interview = form.save(commit=False)
            new_interview.owner = request.user
            new_interview.save()
            return redirect('interview_organizer:index')
    else:
        form = InterviewForm()
    context = {'form': form}
    return render(request, 'new_interview.html', context)

@login_required
def edit_interview(request, interview_id):
    """Page for editing existing interview."""
    interview = get_object_or_404(Interview, id=interview_id, owner=request.user)
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('interview_organizer:interview', interview_id=interview.id)
    else:
        form = InterviewForm(instance=interview)
    context = {'form': form, 'interview': interview}
    return render(request, 'edit_interview.html', context)

@login_required
def delete_interview(request, interview_id):
    """Delete interview."""
    interview = get_object_or_404(Interview, id=interview_id, owner=request.user)
    
    # Check if the user is the owner of the interview
    if interview.owner != request.user:
        return HttpResponseForbidden("You don't have permission to delete this interview.")
    
    # Delete the interview
    interview.delete()
    
    # Redirect back to the index page
    return redirect('interview_organizer:index')
