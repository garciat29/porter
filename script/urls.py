from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_name>/<int:script_id>', views.index, name='index'),
    path('<str:project_name>/<int:script_id>/run_script',views.run_script, name='run_script'),
]
