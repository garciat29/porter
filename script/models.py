from djongo import models

class Script(models.Model):
    name=models.CharField(max_length=100)
    script_id=models.IntegerField(primary_key=True)
    '''
    input_datasets=models.ArrayModelField(
        dataset_id=models.IntegerField()
    )
    '''
    code=models.TextField()
    output=models.IntegerField()
    file_path=models.CharField(max_length=512)
    project=models.CharField(max_length=100)
    def __str__(self):
        return self.name
