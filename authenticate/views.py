from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from authenticate import forms
from authenticate.models import User


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')


#def SignupPage(request):
#    form = forms.SignupForm()
#    if request.method == 'POST':
#        form = forms.SignupForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            #auto-login user
#            login(request, user)
#            return redirect(settings.LOGIN_REDIRECT_URL)
#    return render(request, 'register.html', context={'form': form})


def LoginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                message = 'Identifiants invalides.'

    return render(request, 'login.html', context={'form': form, 'message': message})