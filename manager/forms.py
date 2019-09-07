from django import forms
from manager.models import Project

class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name'] 
