from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Project

#Main page lists all project and allows you to create new ones
#Display all projects plus a blank name??
#GET Index- main. POST(id) adds new project

def index(request):
    try:
        project_list=Project.objects.all()
    except:
        project_list=[]
    return HttpResponse('a v. good admin')

