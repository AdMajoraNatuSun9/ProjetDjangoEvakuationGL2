from django.shortcuts import render
from Teacher import forms
from Teacher.models import Project


# Create your views here.
def homeTeacher(request):

    return render(request, 'homeTeacher.html')


def projet(request):
    form = forms.ProjectForm()
    message = ''
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.create(
                nom=form.cleaned_data['nom'],
                description=form.cleaned_data['description'],
                projet=form.cleaned_data['projet'],
            )
        else:
            message = 'Identifiants invalides.'
    return render(request, 'project.html', context={'form': form, 'message': message})


def liste(request):
    projet = Project.objects.all()
    return render(request, 'listProject.html', context={'projet':projet})