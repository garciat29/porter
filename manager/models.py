from django.db import models

class Project(models.Model):
    name=models.CharField(max_length=100)
    project_id=models.IntegerField(primary_key=True)
    script_repo=models.CharField(max_length=250)
    dataset_repo=models.CharField(max_length=250)

    def __str__(self):
        return self.name   
