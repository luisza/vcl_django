from __future__ import unicode_literals

from django.db import models
from compute.models import Computer, Computerloadstate
from image.models import Image, Imagerevision
from core.models import Module, Affiliation
from authentication.models import User
from reservations.models import Reservation
from managementnode.models import Managementnode
from provisioning.models import Resource

class Log(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    nowfuture = models.CharField(max_length=6)
    start = models.DateTimeField()
    loaded = models.DateTimeField(blank=True, null=True)
    initialend = models.DateTimeField()
    finalend = models.DateTimeField()
    wasavailable = models.IntegerField()
    ending = models.CharField(max_length=10)
    requestid = models.IntegerField(blank=True, null=True)
    computerid = models.ForeignKey(Computer, db_column='computerid', blank=True, null=True)
    remoteip = models.CharField(db_column='remoteIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    imageid = models.ForeignKey(Image, db_column='imageid')
    size = models.SmallIntegerField()

    class Meta:
        
        db_table = 'log'

# Create your models here.
class Sublog(models.Model):
    logid = models.ForeignKey(Log, db_column='logid')
    imageid = models.ForeignKey(Image, db_column='imageid')
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid')
    computerid = models.ForeignKey(Computer, db_column='computerid', related_name="computeid_rel")
    ipaddress = models.CharField(db_column='IPaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    managementnodeid = models.ForeignKey(Managementnode, db_column='managementnodeid')
    predictivemoduleid = models.ForeignKey(Module, db_column='predictivemoduleid')
    hostcomputerid = models.ForeignKey(Computer, db_column='hostcomputerid', blank=True, null=True, related_name="hostcompute_rel")
    blockrequestid = models.IntegerField(db_column='blockRequestid')  # Field name made lowercase.
    blockstart = models.DateTimeField(db_column='blockStart')  # Field name made lowercase.
    blockend = models.DateTimeField(db_column='blockEnd')  # Field name made lowercase.

    class Meta:
        
        db_table = 'sublog'

class Loginlog(models.Model):
    user = models.CharField(max_length=50)
    authmech = models.CharField(max_length=30)
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')
    timestamp = models.DateTimeField()
    passfail = models.IntegerField()
    remoteip = models.CharField(db_column='remoteIP', max_length=15)  # Field name made lowercase.
    code = models.CharField(max_length=19)

    class Meta:
        
        db_table = 'loginlog'

class Querylog(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    timestamp = models.DateTimeField()
    mode = models.CharField(max_length=30)
    query = models.TextField()

    class Meta:
        
        db_table = 'querylog'

class Connectlog(models.Model):
    logid = models.ForeignKey(Log, db_column='logid')
    reservationid = models.IntegerField()
    userid = models.ForeignKey(User, db_column='userid', blank=True, null=True)
    remoteip = models.CharField(db_column='remoteIP', max_length=39)  # Field name made lowercase.
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        
        db_table = 'connectlog'
        unique_together = (('reservationid', 'userid', 'remoteip'),)
        
        
class Computerloadlog(models.Model):
    reservationid = models.ForeignKey(Reservation, db_column='reservationid')
    computerid = models.ForeignKey(Computer, db_column='computerid')
    loadstateid = models.ForeignKey(Computerloadstate, db_column='loadstateid')
    timestamp = models.DateTimeField(blank=True, null=True)
    additionalinfo = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'computerloadlog'

class Changelog(models.Model):
    logid = models.ForeignKey(Log, db_column='logid')
    userid = models.ForeignKey(User, db_column='userid', blank=True, null=True)
    reservationid = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    computerid = models.ForeignKey(Computer, db_column='computerid', blank=True, null=True)
    remoteip = models.CharField(db_column='remoteIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    wasavailable = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    other = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'changelog'
        unique_together = (('userid', 'reservationid', 'remoteip'),)
        
class Xmlrpclog(models.Model):
    xmlrpckeyid = models.SmallIntegerField(db_column='xmlrpcKeyid')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ipaddress = models.CharField(db_column='IPaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(max_length=60, blank=True, null=True)
    apiversion = models.IntegerField()
    comments = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'xmlrpcLog'
        


class Natlog(models.Model):
    sublogid = models.ForeignKey(Sublog, db_column='sublogid')
    nathostresourceid = models.ForeignKey(Resource, db_column='nathostresourceid')
    publicipaddress = models.CharField(db_column='publicIPaddress', max_length=15)  # Field name made lowercase.
    publicport = models.SmallIntegerField()
    internalipaddress = models.CharField(db_column='internalIPaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    internalport = models.SmallIntegerField()
    protocol = models.CharField(max_length=3)
    timestamp = models.DateTimeField()

    class Meta:
        
        db_table = 'natlog'
        unique_together = (('sublogid', 'nathostresourceid', 'publicipaddress', 'publicport', 'internalipaddress', 'internalport', 'protocol'),)
