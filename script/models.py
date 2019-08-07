#from django.db import models
from neo4django.db import models

class Script(models.NodeModel):
    name=models.StringProperty()
    owners=models.ArrayProperty()
    input_datasets=models.ArrayProperty()
    #change to relationship tp a dataset node
    output=models.IntegerProperty()
    file_path=models.StringProperty()

# Create your models here.
