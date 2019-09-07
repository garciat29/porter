from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Project
from .forms import NewProject
#Main page lists all project and allows you to create new ones
#Display all projects plus a blank name??
#GET Index- main. POST(id) adds new project

def index(request):
    try:
        project_list=Project.objects.all()
    except:
        project_list=[]
    template = loader.get_template('manager/index.html')
    context = {'project_list': project_list}
    return render(request, 'manager/index.html', context)
    #return HttpResponse('a v. good admin')

