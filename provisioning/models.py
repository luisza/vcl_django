from __future__ import unicode_literals

from django.db import models
from core.models import Module, Osinstalltype, Privnode, Affiliation
from authentication.models import Usergroup
# Create your models here.

class Provisioning(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    prettyname = models.CharField(max_length=70)
    moduleid = models.ForeignKey(Module, db_column='moduleid')

    class Meta:
        
        db_table = 'provisioning'


class Provisioningosinstalltype(models.Model):
    provisioningid = models.ForeignKey(Provisioning, db_column='provisioningid')
    osinstalltypeid = models.ForeignKey(Osinstalltype, db_column='OSinstalltypeid')  # Field name made lowercase.

    class Meta:
        
        db_table = 'provisioningOSinstalltype'
        unique_together = (('provisioningid', 'osinstalltypeid'),)


class Resourcetype(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        
        db_table = 'resourcetype'

class Resource(models.Model):
    resourcetypeid = models.ForeignKey(Resourcetype, db_column='resourcetypeid')
    subid = models.IntegerField()

    class Meta:
        
        db_table = 'resource'
        unique_together = (('resourcetypeid', 'subid'),)


class Resourcegroup(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    ownerusergroupid = models.ForeignKey(Usergroup, db_column='ownerusergroupid')
    resourcetypeid = models.ForeignKey(Resourcetype, db_column='resourcetypeid')

    class Meta:
        
        db_table = 'resourcegroup'
        unique_together = (('resourcetypeid', 'name'),)


class Resourcegroupmembers(models.Model):
    resourceid = models.ForeignKey(Resource, db_column='resourceid')
    resourcegroupid = models.ForeignKey(Resourcegroup, db_column='resourcegroupid')

    class Meta:
        
        db_table = 'resourcegroupmembers'
        unique_together = (('resourceid', 'resourcegroupid'),)


class Resourcemap(models.Model):
    resourcegroupid1 = models.ForeignKey(Resourcegroup, db_column='resourcegroupid1', related_name ="R1" )
    resourcetypeid1 = models.ForeignKey(Resourcetype, db_column='resourcetypeid1', related_name ="R2" )
    resourcegroupid2 = models.ForeignKey(Resourcegroup, db_column='resourcegroupid2', related_name ="R3")
    resourcetypeid2 = models.ForeignKey(Resourcetype, db_column='resourcetypeid2', related_name ="R4")

    class Meta:
        
        db_table = 'resourcemap'
        unique_together = (('resourcegroupid1', 'resourcegroupid2'),)


class Resourcepriv(models.Model):
    resourcegroupid = models.ForeignKey(Resourcegroup, db_column='resourcegroupid')
    privnodeid = models.ForeignKey(Privnode, db_column='privnodeid')
    type = models.CharField(max_length=13)

    class Meta:
        
        db_table = 'resourcepriv'
        unique_together = (('resourcegroupid', 'privnodeid', 'type'),)


class Statgraphcache(models.Model):
    graphtype = models.CharField(max_length=11)
    statdate = models.DateField()
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid', blank=True, null=True)
    value = models.IntegerField()
    provisioningid = models.ForeignKey(Provisioning, db_column='provisioningid', blank=True, null=True)

    class Meta:
        
        db_table = 'statgraphcache'

