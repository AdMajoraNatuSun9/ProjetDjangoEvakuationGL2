from django import forms


class TeacherForm(forms.Form):
    nom = forms.CharField(label='nom',widget=forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='prenom',widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    dateNaissance = forms.DateField(label='dateNaissance',widget=forms.DateInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(label='numero',widget=forms.TextInput(attrs={'class': 'form-control'}))


class StudentForm(forms.Form):
    nom = forms.CharField(label='nom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label='prenom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(label='numero', widget=forms.TextInput(attrs={'class': 'form-control'}))
    matiere = forms.ChoiceField(label='matiere', widget=forms.CheckboxInput(attrs={'class': 'form-control'}))