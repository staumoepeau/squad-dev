from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm, AdminLoginForm


#@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Redirect to a page where the user can create their profile
        return redirect('create_profile')  # Assuming you have a URL named 'create_profile'
    
    return render(request, 'users/profile.html', {'profile': profile})

def update_profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'users/update-profile.html', context)

def applogin(request):
    msg = ""
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Invalid credentials'
        else:
            msg = "Error Validating the form"
                
    context = {'forms': forms, 'msg': msg}
    
    return render(request, 'users/login.html', context)

def applogout(request):
    logout(request)
    return redirect('login')
