from __future__ import unicode_literals

from django.db import models
from authentication.models import User, Usergroup
from compute.models import Computer
from image.models import Image, Imagerevision
from managementnode.models import Managementnode
from core.models import State


class Request(models.Model):
    stateid = models.ForeignKey(State, db_column='stateid', related_name="rel_si")
    userid = models.ForeignKey(User, db_column='userid')
    laststateid = models.ForeignKey(State, db_column='laststateid', related_name="rel_laststateid" )
    logid = models.IntegerField()
    forimaging = models.IntegerField()
    test = models.IntegerField()
    preload = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    daterequested = models.DateTimeField()
    datemodified = models.DateTimeField(blank=True, null=True)
    checkuser = models.IntegerField()

    class Meta:
        
        db_table = 'request'

class Serverrequest(models.Model):
    name = models.CharField(max_length=255)
    serverprofileid = models.SmallIntegerField()
    requestid = models.OneToOneField(Request, db_column='requestid')
    fixedip = models.CharField(db_column='fixedIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fixedmac = models.CharField(db_column='fixedMAC', max_length=17, blank=True, null=True)  # Field name made lowercase.
    admingroupid = models.ForeignKey(Usergroup, db_column='admingroupid', blank=True, null=True, related_name="rel_agi")
    logingroupid = models.ForeignKey(Usergroup, db_column='logingroupid', blank=True, null=True, related_name="rel_login")
    monitored = models.IntegerField()

    class Meta:
        
        db_table = 'serverrequest'

# Create your models here.
class Reservation(models.Model):
    requestid = models.ForeignKey(Request, db_column='requestid')
    computerid = models.ForeignKey(Computer, db_column='computerid')
    imageid = models.ForeignKey(Image, db_column='imageid')
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid')
    managementnodeid = models.ForeignKey(Managementnode, db_column='managementnodeid')
    remoteip = models.CharField(db_column='remoteIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastcheck = models.DateTimeField(blank=True, null=True)
    pw = models.CharField(max_length=40, blank=True, null=True)
    connectip = models.CharField(db_column='connectIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    connectport = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'reservation'
        
class Reservationaccounts(models.Model):
    reservationid = models.ForeignKey(Reservation, db_column='reservationid')
    userid = models.ForeignKey(User, db_column='userid')
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'reservationaccounts'
        unique_together = (('reservationid', 'userid'),)
