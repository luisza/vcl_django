from __future__ import unicode_literals

from django.db import models
from compute.models import Computer
from image.models import Imagerevision
# Create your models here.

class Openstackcomputermap(models.Model):
    instanceid = models.CharField(primary_key=True, max_length=50)
    computerid = models.OneToOneField(Computer, db_column='computerid', blank=True, null=True)

    class Meta:
        
        db_table = 'openstackcomputermap'


class Openstackimagerevision(models.Model):
    imagerevisionid = models.OneToOneField(Imagerevision, db_column='imagerevisionid', primary_key=True)
    imagedetails = models.TextField()
    flavordetails = models.TextField()

    class Meta:
        
        db_table = 'openstackimagerevision'
