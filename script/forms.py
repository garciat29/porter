from django import forms


class ScriptInput(forms.Form):
    name = forms.CharField(label='Script Name', max_length=100)
    code = forms.CharField(widget=forms.Textarea)  
