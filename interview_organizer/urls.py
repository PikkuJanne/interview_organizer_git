from django.urls import path
from . import views

app_name = 'interview_organizer'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Upcoming interviews
    path('upcoming/', views.upcoming, name='upcoming'),
    #Interview archive
    path('archive/', views.archive, name='archive'),
    #Page for single interview
    path('interviews/<int:interview_id>/', views.interview, name='interview'),
    # Page for questions of an interview
    path('interviews/<int:interview_id>/questions/', views.questions, name='questions'),
    path('new_interview/', views.new_interview, name='new_interview'),
    path('interviews/<int:interview_id>/edit/', views.edit_interview, name='edit_interview'),
    path('delete_interview/<int:interview_id>/', views.delete_interview, name='delete_interview'),
]