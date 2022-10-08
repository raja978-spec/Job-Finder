from django.db import models

# Create your models here.
class Jobs(models.Model):
    title=models.CharField(null=False,max_length=10000000)
    location=models.CharField(null=False,max_length=10000000)
    time=models.CharField(null=False,max_length=10000000)
    link=models.CharField(null=False,max_length=10000000)
    caption=models.CharField(null=False,max_length=10000000,default='')

class DefaultJobs(models.Model):
    title=models.CharField(null=False,max_length=10000000)
    location=models.CharField(null=False,max_length=10000000)
    time=models.CharField(null=False,max_length=10000000)
    link=models.CharField(null=False,max_length=10000000)
    caption=models.CharField(null=False,max_length=10000000,default='')

class InternShipJobs(models.Model):
    title=models.CharField(null=False,max_length=10000000)
    location=models.CharField(null=False,max_length=10000000)
    time=models.CharField(null=False,max_length=10000000)
    link=models.CharField(null=False,max_length=10000000)


