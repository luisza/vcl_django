from __future__ import unicode_literals

from django.db import models
from authentication.models import User
from core.models import State
# Create your models here.
from provisioning.models import Resourcegroup

class Managementnode(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    ipaddress = models.CharField(db_column='IPaddress', max_length=15)  # Field name made lowercase.
    hostname = models.CharField(max_length=50)
    ownerid = models.ForeignKey(User, db_column='ownerid')
    stateid = models.ForeignKey(State, db_column='stateid')
    lastcheckin = models.DateTimeField(blank=True, null=True)
    checkininterval = models.IntegerField()
    installpath = models.CharField(max_length=100)
    imagelibenable = models.IntegerField()
    imagelibgroupid = models.ForeignKey(Resourcegroup, db_column='imagelibgroupid', blank=True, null=True)
    imagelibuser = models.CharField(max_length=20, blank=True, null=True)
    imagelibkey = models.CharField(max_length=100, blank=True, null=True)
    keys = models.CharField(max_length=1024, blank=True, null=True)
    sshport = models.SmallIntegerField()
    publicipconfiguration = models.CharField(db_column='publicIPconfiguration', max_length=11)  # Field name made lowercase.
    publicsubnetmask = models.CharField(db_column='publicSubnetMask', max_length=56, blank=True, null=True)  # Field name made lowercase.
    publicdefaultgateway = models.CharField(db_column='publicDefaultGateway', max_length=56, blank=True, null=True)  # Field name made lowercase.
    publicdnsserver = models.CharField(db_column='publicDNSserver', max_length=56, blank=True, null=True)  # Field name made lowercase.
    sysadminemailaddress = models.CharField(db_column='sysadminEmailAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sharedmailbox = models.CharField(db_column='sharedMailBox', max_length=128, blank=True, null=True)  # Field name made lowercase.
    not_standalone = models.CharField(db_column='NOT_STANDALONE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    availablenetworks = models.TextField()

    class Meta:
        
        db_table = 'managementnode'
