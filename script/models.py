#from django.db import models
from djongo import models

class Script(models.Model):
    _id=models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=100)
    '''
    input_datasets=models.ArrayModelField(
        dataset_id=models.IntegerField()
    )
    '''
    code=models.TextField()
    output=models.IntegerField()
    file_path=models.CharField(max_length=512)

    def __str__(self):
        return self.name
