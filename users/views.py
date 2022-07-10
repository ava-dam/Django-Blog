from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegisterForm, UserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
#imports the form to create a new user ^^


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saves user, hashes password to make secure
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) 

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



# get requests: things you send while navigating the page
# post requests: the form does nothing cause we don't post the form data anywhere 
# flash message: update base template to add flash message
# bootstrap and django message names are the same 
# decorators add functionality; login_required will deny access to /profile/ unless logged in
'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''