from django import forms


class ProjectForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    projet = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
