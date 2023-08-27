from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from authenticate.models import Student, Teacher
from Course import forms
# Create your views here.


def create_Teacher(request):
    form = forms.TeacherForm()
    message = ''
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.create(
                nom = form.cleaned_data['nom'],
                prenom = form.cleaned_data['prenom'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                dateNaissance = form.cleaned_data['dateNaissance'],
                numero = form.cleaned_data['numero']
            )
        else:
            message = 'Identifiants invalides.'
    return render(request, 'formEnseignant.html', context={'form': form, 'message': message})


def show_Teachers(request, id):
    teachers = Teacher.objects.all()
    return render(request, 'formEnseignant.html', {'teachers': teachers, 'id': get_object_or_404(Teacher, id=id)})


def update_Teachers(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createTeacher')  # Redirect to the teacher list view or another appropriate page
    else:
        form = forms.TeacherForm()

    return render(request, 'formEnseignant.html', {'form': form, 'id': teacher})


def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.delete()
        return redirect('createTeacher')  # Redirect to the teacher list view or another appropriate page

    return render(request, 'formEnseignant.html', {'teacher': teacher})


def create_Student(request):
    form = forms.StudentForm()
    message = ''
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.create(
                nom=form.cleaned_data['nom'],
                prenom=form.cleaned_data['prenom'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                dateNaissance=form.cleaned_data['dateNaissance'],
                numero=form.cleaned_data['numero'],
                matiere=form.cleaned_data['matiere']
            )
        else:
            message = 'Identifiants invalides.'
    return render(request, 'formEtudiant.html', context={'form': form, 'message': message})

def create_course(request):
    return render(request, 'formMatière.html')

