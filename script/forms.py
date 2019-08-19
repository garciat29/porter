from django import forms
from script.models import Script
'''
class ScriptInput(forms.Form):
    name = forms.CharField(label='Script Name', max_length=100)
    code = forms.CharField(widget=forms.Textarea)
'''

class ScriptInput(forms.ModelForm):
    class Meta:
        model = Script
        fields=['name','code', 'output']
