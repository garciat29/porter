from django.shortcuts import get_object_or_404, render, redirect 
from django.http import HttpResponse, HttpResponseRedirect

from .models import Script
from .forms import ScriptInput

def index(request, script_id, project_name):
    try:
        curr_script=Script.objects.get(pk=script_id)
    except:
        curr_script=Script()
    if request.method=='POST':
        curr_script.script_id=script_id
        curr_script.project=project_name
        form = ScriptInput(request.POST,instance=curr_script)
        if form.is_valid():
            save_req=form.save(commit=False)
            save_req.save()
            #form.save()
    else:
        form= ScriptInput(instance=curr_script)
        #context = {'script_id':script_id, 'script_code':script.code, 'script_name':script.name }
    context={'form':form,'script_id':script_id,'project_name':project_name}
    return render(request, 'script/index.html', context)
