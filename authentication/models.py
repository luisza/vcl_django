from __future__ import unicode_literals

from django.db import models
from core.models import Imtype, Affiliation, Privnode
# Create your models here.

class User(models.Model):
    uid = models.IntegerField(unique=True, blank=True, null=True)
    unityid = models.CharField(max_length=80)
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=25)
    preferredname = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=80)
    emailnotices = models.IntegerField()
    imtypeid = models.ForeignKey(Imtype, db_column='IMtypeid')  # Field name made lowercase.
    imid = models.CharField(db_column='IMid', max_length=80, blank=True, null=True)  # Field name made lowercase.
    adminlevelid = models.IntegerField()
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    bpp = models.IntegerField()
    audiomode = models.CharField(max_length=5)
    mapdrives = models.IntegerField()
    mapprinters = models.IntegerField()
    mapserial = models.IntegerField()
    rdpport = models.SmallIntegerField(blank=True, null=True)
    showallgroups = models.IntegerField()
    lastupdated = models.DateTimeField()
    validated = models.IntegerField()
    usepublickeys = models.IntegerField()
    sshpublickeys = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'user'
        unique_together = (('unityid', 'affiliationid'),)


class Usergroup(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid', blank=True, null=True)
    ownerid = models.ForeignKey(User, db_column='ownerid', blank=True, null=True)
    editusergroupid = models.ForeignKey('self', db_column='editusergroupid', blank=True, null=True)
    custom = models.IntegerField()
    courseroll = models.IntegerField()
    initialmaxtime = models.SmallIntegerField()
    totalmaxtime = models.SmallIntegerField()
    maxextendtime = models.SmallIntegerField()
    overlaprescount = models.SmallIntegerField(db_column='overlapResCount')  # Field name made lowercase.

    class Meta:
        
        db_table = 'usergroup'
        unique_together = (('name', 'affiliationid'),)

class Usergroupmembers(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    usergroupid = models.ForeignKey(Usergroup, db_column='usergroupid')

    class Meta:
        
        db_table = 'usergroupmembers'
        unique_together = (('userid', 'usergroupid'),)


class Usergrouppriv(models.Model):
    usergroupid = models.ForeignKey(Usergroup, db_column='usergroupid')
    userprivtypeid = models.ForeignKey('Usergroupprivtype', db_column='userprivtypeid')

    class Meta:
        
        db_table = 'usergrouppriv'
        unique_together = (('usergroupid', 'userprivtypeid'),)


class Usergroupprivtype(models.Model):
    name = models.CharField(max_length=50)
    help = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'usergroupprivtype'


class Userpriv(models.Model):
    #id = models.AutoField()
    userid = models.ForeignKey(User, db_column='userid', blank=True, null=True)
    usergroupid = models.ForeignKey(Usergroup, db_column='usergroupid', blank=True, null=True)
    privnodeid = models.ForeignKey(Privnode, db_column='privnodeid')
    userprivtypeid = models.ForeignKey('Userprivtype', db_column='userprivtypeid')

    class Meta:
        
        db_table = 'userpriv'
        unique_together = (('userid', 'privnodeid', 'userprivtypeid'),)


class Userprivtype(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        
        db_table = 'userprivtype'


class Shibauth(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    ts = models.DateTimeField()
    sessid = models.CharField(max_length=80)
    data = models.TextField()

    class Meta:
        
        db_table = 'shibauth'

class Localauth(models.Model):
    userid = models.OneToOneField(User, db_column='userid', primary_key=True)
    passhash = models.CharField(max_length=40)
    salt = models.CharField(max_length=8)
    lastupdated = models.DateTimeField()
    lockedout = models.IntegerField()

    class Meta:
        
        db_table = 'localauth'
