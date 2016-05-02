from __future__ import unicode_literals

from django.db import models
from core.models import State, Platform, Module
from image.models import Image, Imagerevision, Imagetype
from provisioning.models import Provisioning
from authentication.models import User, Usergroup
from managementnode.models import Managementnode
# Create your models here.

class Schedule(models.Model):
    name = models.CharField(unique=True, max_length=25)
    ownerid = models.ForeignKey(User, db_column='ownerid')

    class Meta:
        
        db_table = 'schedule'

class Scheduletimes(models.Model):
    scheduleid = models.ForeignKey(Schedule, db_column='scheduleid')
    start = models.SmallIntegerField()
    end = models.SmallIntegerField()

    class Meta:
        
        db_table = 'scheduletimes'


class Computer(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    stateid = models.ForeignKey(State, db_column='stateid')
    ownerid = models.ForeignKey(User, db_column='ownerid', blank=True, null=True)
    platformid = models.ForeignKey(Platform, db_column='platformid')
    scheduleid = models.ForeignKey(Schedule, db_column='scheduleid', blank=True, null=True)
    # ok down is instanced
    vmhostid = models.ForeignKey('Vmhost', db_column='vmhostid', blank=True, null=True)
    currentimageid = models.ForeignKey(Image, db_column='currentimageid', related_name="rel_currentimageid")
    nextimageid = models.ForeignKey(Image, db_column='nextimageid', related_name="rel_nextimageid")
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid')
    ram = models.IntegerField(db_column='RAM')  # Field name made lowercase.
    procnumber = models.IntegerField()
    procspeed = models.SmallIntegerField()
    network = models.SmallIntegerField()
    hostname = models.CharField(max_length=36)
    ipaddress = models.CharField(db_column='IPaddress', max_length=15)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='privateIPaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    eth0macaddress = models.CharField(max_length=17, blank=True, null=True)
    eth1macaddress = models.CharField(max_length=17, blank=True, null=True)
    type = models.CharField(max_length=14)
    provisioningid = models.ForeignKey(Provisioning, db_column='provisioningid')
    drivetype = models.CharField(max_length=4)
    deleted = models.IntegerField()
    datedeleted = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    lastcheck = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    dsa = models.TextField(blank=True, null=True)
    dsapub = models.TextField(blank=True, null=True)
    rsa = models.TextField(blank=True, null=True)
    rsapub = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    hostpub = models.TextField(blank=True, null=True)
    vmtypeid = models.IntegerField(blank=True, null=True)
    predictivemoduleid = models.ForeignKey(Module, db_column='predictivemoduleid')

    class Meta:
        
        db_table = 'computer'
        unique_together = (('eth1macaddress', 'datedeleted'), ('hostname', 'datedeleted'), ('eth0macaddress', 'datedeleted'),)

        
class Vmprofile(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    profilename = models.CharField(unique=True, max_length=56)
    imageid = models.ForeignKey(Image, db_column='imageid')
    resourcepath = models.CharField(max_length=256, blank=True, null=True)
    folderpath = models.CharField(max_length=256, blank=True, null=True)
    repositorypath = models.CharField(max_length=128, blank=True, null=True)
    repositoryimagetypeid = models.ForeignKey(Imagetype, db_column='repositoryimagetypeid', related_name="IR1")
    datastorepath = models.CharField(max_length=128)
    datastoreimagetypeid = models.ForeignKey(Imagetype, db_column='datastoreimagetypeid',  related_name="IR3")
    vmpath = models.CharField(max_length=128, blank=True, null=True)
    virtualswitch0 = models.CharField(max_length=80)
    virtualswitch1 = models.CharField(max_length=80)
    virtualswitch2 = models.CharField(max_length=80, blank=True, null=True)
    virtualswitch3 = models.CharField(max_length=80, blank=True, null=True)
    vmdisk = models.CharField(max_length=9)
    username = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    eth0generated = models.IntegerField()
    eth1generated = models.IntegerField()
    rsapub = models.TextField(blank=True, null=True)
    rsakey = models.CharField(max_length=256, blank=True, null=True)
    encryptedpasswd = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'vmprofile'
        
        
class Vmhost(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    computerid = models.OneToOneField(Computer, db_column='computerid')
    vmlimit = models.IntegerField()
    vmprofileid = models.ForeignKey(Vmprofile, db_column='vmprofileid')

    class Meta:
        
        db_table = 'vmhost'
        

class Computerloadstate(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    loadstatename = models.CharField(unique=True, max_length=24)
    prettyname = models.CharField(max_length=50, blank=True, null=True)
    est = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'computerloadstate'

class Computerloadflow(models.Model):
    computerloadstateid = models.ForeignKey(Computerloadstate, db_column='computerloadstateid', related_name="clsi")
    nextstateid = models.ForeignKey(Computerloadstate, db_column='nextstateid', blank=True, null=True, related_name="nsi")
    type = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        
        db_table = 'computerloadflow'



class Blockrequest(models.Model):
    name = models.CharField(max_length=80)
    imageid = models.ForeignKey(Image, db_column='imageid')
    nummachines = models.IntegerField(db_column='numMachines')  # Field name made lowercase.
    groupid = models.ForeignKey(Usergroup, db_column='groupid', blank=True, null=True)
    repeating = models.CharField(max_length=7)
    ownerid = models.ForeignKey(User, db_column='ownerid')
    managementnodeid = models.ForeignKey(Managementnode, db_column='managementnodeid', blank=True, null=True)
    expiretime = models.DateTimeField(db_column='expireTime')  # Field name made lowercase.
    processing = models.IntegerField()
    status = models.CharField(max_length=9)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'blockRequest'


class Blocktimes(models.Model):
    blockrequestid = models.ForeignKey(Blockrequest, db_column='blockRequestid')  # Field name made lowercase.
    start = models.DateTimeField()
    end = models.DateTimeField()
    processed = models.IntegerField()
    skip = models.IntegerField()

    class Meta:
        
        db_table = 'blockTimes'
        
class Blockcomputers(models.Model):
    blocktimeid = models.ForeignKey(Blocktimes, db_column='blockTimeid')  # Field name made lowercase.
    computerid = models.ForeignKey(Computer, db_column='computerid')
    imageid = models.ForeignKey(Image, db_column='imageid')
    reloadrequestid = models.IntegerField()

    class Meta:
        
        db_table = 'blockComputers'
        unique_together = (('blocktimeid', 'computerid'),)



class Blockwebdate(models.Model):
    blockrequestid = models.ForeignKey(Blockrequest, db_column='blockRequestid')  # Field name made lowercase.
    start = models.DateField()
    end = models.DateField()
    days = models.IntegerField(blank=True, null=True)
    weeknum = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'blockWebDate'


class Blockwebtime(models.Model):
    blockrequestid = models.ForeignKey(Blockrequest, db_column='blockRequestid')  # Field name made lowercase.
    starthour = models.IntegerField()
    startminute = models.IntegerField()
    startmeridian = models.CharField(max_length=2)
    endhour = models.IntegerField()
    endminute = models.IntegerField()
    endmeridian = models.CharField(max_length=2)
    order = models.IntegerField()

    class Meta:
        
        db_table = 'blockWebTime'

class Semaphore(models.Model):
    computerid = models.ForeignKey(Computer, db_column='computerid')
    imageid = models.ForeignKey(Image, db_column='imageid')
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid')
    managementnodeid = models.ForeignKey(Managementnode, db_column='managementnodeid')
    expires = models.DateTimeField()
    procid = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'semaphore'

class Serverprofile(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    imageid = models.ForeignKey(Image, db_column='imageid')
    ownerid = models.ForeignKey(User, db_column='ownerid')
    ending = models.CharField(max_length=10)
    fixedip = models.CharField(db_column='fixedIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fixedmac = models.CharField(db_column='fixedMAC', max_length=17, blank=True, null=True)  # Field name made lowercase.
    admingroupid = models.ForeignKey(Usergroup, db_column='admingroupid', blank=True, null=True, related_name="agi" )
    logingroupid = models.ForeignKey(Usergroup, db_column='logingroupid', blank=True, null=True, related_name="lalog")
    monitored = models.IntegerField()

    class Meta:
        
        db_table = 'serverprofile'
        
class Clickthroughs(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    imageid = models.ForeignKey(Image, db_column='imageid')
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid', blank=True, null=True)
    accepted = models.DateTimeField()
    agreement = models.TextField()

    class Meta:
        
        db_table = 'clickThroughs'

