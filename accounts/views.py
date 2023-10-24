from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    """Register new user."""
    if request.method != 'POST':
        #Display blank registration form.
        form = UserCreationForm()
    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log user in and then redirect to home page.
            login(request, new_user)
            return redirect('interview_organizer:index')
    
    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete the user account
        request.user.delete()
        # Logout the user
        logout(request)
        return redirect('interview_organizer:index')
    return render(request, 'accounts/delete_account_confirm.html')
