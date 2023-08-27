from django import forms


class ProjectForm(forms.Form):
    nom = forms.CharField(label='nom',widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label='description',widget=forms.TextInput(attrs={'class': 'form-control'}))
    projet = forms.FileField(label='projet', widget=forms.FileInput(attrs={'class': 'form-control'}))
