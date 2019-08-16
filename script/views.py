from django.shortcuts import get_object_or_404,  render 
from django.http import HttpResponse, HttpResponseRedirect

from .models import Script
from .forms import ScriptInput

def index(request, script_id, project_name):
    if request.method=='POST':
        form = ScriptInput(request.POST)
    else:
        form= ScriptInput()
        #context = {'script_id':script_id, 'script_code':script.code, 'script_name':script.name }
    context={'form':form,'script_id':script_id,'project_name':project_name}
    return render(request, 'script/index.html', context)
