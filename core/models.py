from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Imtype(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        
        db_table = 'IMtype'

class State(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        
        db_table = 'state'

class Platform(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        
        db_table = 'platform'



class Module(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    prettyname = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    perlpackage = models.CharField(max_length=150)

    class Meta:
        
        db_table = 'module'
        
class Osinstalltype(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        
        db_table = 'OSinstalltype'
        
class Affiliation(models.Model):
    name = models.CharField(unique=True, max_length=40)
    shibname = models.CharField(max_length=60, blank=True, null=True)
    dataupdatetext = models.TextField(db_column='dataUpdateText')  # Field name made lowercase.
    sitewwwaddress = models.CharField(max_length=56, blank=True, null=True)
    helpaddress = models.CharField(max_length=32, blank=True, null=True)
    shibonly = models.IntegerField()
    theme = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'affiliation'
        
class Privnode(models.Model):
    parent = models.ForeignKey('self', db_column='parent')
    name = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'privnode'
        unique_together = (('parent', 'name'),)

## Those models are not related
class Variable(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    serialization = models.CharField(max_length=12)
    value = models.TextField()
    setby = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        
        db_table = 'variable'
        
class Continuations(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    userid = models.IntegerField()
    expiretime = models.DateTimeField()
    frommode = models.CharField(max_length=50)
    tomode = models.CharField(max_length=50)
    data = models.TextField()
    multicall = models.IntegerField()
    parentid = models.ForeignKey('self', db_column='parentid', blank=True, null=True)
    deletefromid = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'continuations'
        
class Adminlevel(models.Model):
    name = models.CharField(unique=True, max_length=10)

    class Meta:
        
        db_table = 'adminlevel'

class Documentation(models.Model):
    name = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    data = models.TextField()

    class Meta:
        
        db_table = 'documentation'


class Sitemaintenance(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    ownerid = models.IntegerField()
    created = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)
    usermessage = models.TextField()
    informhoursahead = models.SmallIntegerField()
    allowreservations = models.IntegerField()

    class Meta:
        
        db_table = 'sitemaintenance'

