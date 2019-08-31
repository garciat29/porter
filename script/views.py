import subprocess

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
    else:
        form= ScriptInput(instance=curr_script)
    context={'form':form,'script_id':script_id,'project_name':project_name}
    return render(request, 'script/index.html', context)

def run_script(request, script_id, project_name):
    script_home='/home/ec2-user/script_repo/'
    test_output='/home/ec2-user/local_data/'
    try:
        curr_script=Script.objects.get(pk=script_id)
    except:
        return HttpResponse('Script not found')
    if request.method=='POST':
        curr_code=curr_script.code
        script_name=curr_script.name
        local_script=script_home+script_name
        out_data=test_output+'init_test.txt'
        with open(local_script, 'w+') as s:
            s.write(curr_code)
        result= subprocess.run(['python',local_script], stdout=subprocess.PIPE)
        with open(out_data, 'wb+') as o:
            o.write(result.stdout)
        
    return HttpResponse(curr_code)

