from django.urls import path

from . import views

urlpatterns = [
    path('<int:script_id>', views.index, name='index'),
    path('<int:script_id>/save', views.save_script, name='save_script'),
]
