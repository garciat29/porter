from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_name>/<int:script_id>', views.index, name='index'),
]
