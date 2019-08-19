from djongo import models

class Platform(models.Model):
    #Describes the type of service used to host the data
    #e.g. file server, Oracle DB, Box, etc
    name=models.CharField(max_length=100)
    platform_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    #Credentials and location for an object that contains datasets
    #Examples are file servers, database, cloud based tools
    #Encapsulates info needed to access the account
    name=models.CharField(max_length=100)
    account_id=models.IntegerField(primary_key=True)
    platform=models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL)     

    def __str__(self):
        return self.name 

class Source(models.Model):
    #represents the specific data location from an account
    #e.g. File path on an FTP account, schema+table on db
    name=models.CharField(max_length=100)
    source_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    name=models.CharField(max_length=100)
    dataset_id=models.IntegerField(primary_key=True)
    #change to FK relationship to an admin accounts table
    account=models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    #change to FK relationship to have FK relationship with account
    source=models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
