from __future__ import unicode_literals

from django.db import models
from compute.models import Computer
from image.models import Connectmethodport
from provisioning.models import Resource
from reservations.models import Reservation

# Create your models here.

class Nathost(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    resourceid = models.OneToOneField(Resource, db_column='resourceid')
    publicipaddress = models.CharField(db_column='publicIPaddress', max_length=15)  # Field name made lowercase.
    internalipaddress = models.CharField(db_column='internalIPaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'nathost'


class Nathostcomputermap(models.Model):
    nathostid = models.ForeignKey(Nathost, db_column='nathostid')
    computerid = models.ForeignKey(Computer, db_column='computerid')

    class Meta:
        
        db_table = 'nathostcomputermap'
        unique_together = (('computerid', 'nathostid'),)


class Natport(models.Model):
    reservationid = models.ForeignKey(Reservation, db_column='reservationid')
    nathostid = models.ForeignKey(Nathost, db_column='nathostid')
    publicport = models.SmallIntegerField()
    connectmethodportid = models.ForeignKey(Connectmethodport, db_column='connectmethodportid')

    class Meta:
        
        db_table = 'natport'
        unique_together = (('nathostid', 'publicport'), ('reservationid', 'connectmethodportid'),)
