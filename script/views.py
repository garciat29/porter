from django.shortcuts import get_object_or_404,  render 
from django.http import HttpResponse, HttpResponseRedirect

from .models import Script

def save_script(request,script_id):
    #need url to be the script id
    #on loading page, try to get script, if fails, create a new script, but only save on Save
    print('trying to save!')
    print(request)
    print(script_id)
    #script=Script.objects.get((_id=script_id) 


def index(request, script_id):
    #return HttpResponse("Hello, world. You're at the polls index."
    try:
        script=Script.objects.get(pk=script_id)
    except:
        script=Script(_id=script_id)
    context = {'script_id':script_id, 'script_code':script.code, 'script_name':script.name }
    return render(request, 'script/index.html', context)
