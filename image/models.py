from __future__ import unicode_literals

from django.db import models

from core.models import Platform, Module, Osinstalltype, Affiliation
from authentication.models import User


class Ostype(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        
        db_table = 'OStype'
        

        
class Imagetype(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=16)

    class Meta:
        
        db_table = 'imagetype'


        
# Create your models here.
class Os(models.Model):
    name = models.CharField(unique=True, max_length=20)
    prettyname = models.CharField(unique=True, max_length=64)
    type = models.ForeignKey(Ostype, db_column='type')
    installtype = models.ForeignKey(Osinstalltype, db_column='installtype')
    minram = models.IntegerField()
    sourcepath = models.CharField(max_length=30, blank=True, null=True)
    moduleid = models.ForeignKey(Module, db_column='moduleid', blank=True, null=True)

    class Meta:
        
        db_table = 'OS'

class Imagemeta(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    checkuser = models.IntegerField()
    subimages = models.IntegerField()
    sysprep = models.IntegerField()
    postoption = models.CharField(max_length=32, blank=True, null=True)
    architecture = models.CharField(max_length=10, blank=True, null=True)
    rootaccess = models.IntegerField()
    sethostname = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'imagemeta'

class Image(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=70)
    prettyname = models.CharField(unique=True, max_length=60)
    ownerid = models.ForeignKey(User, db_column='ownerid', blank=True, null=True)
    imagetypeid = models.ForeignKey(Imagetype, db_column='imagetypeid')
    platformid = models.ForeignKey(Platform, db_column='platformid')
    osid = models.ForeignKey(Os, db_column='OSid')  # Field name made lowercase.
    imagemetaid = models.ForeignKey(Imagemeta, db_column='imagemetaid', blank=True, null=True)
    minram = models.IntegerField()
    minprocnumber = models.IntegerField()
    minprocspeed = models.SmallIntegerField()
    minnetwork = models.SmallIntegerField()
    maxconcurrent = models.IntegerField(blank=True, null=True)
    reloadtime = models.IntegerField()
    deleted = models.IntegerField()
    test = models.IntegerField()
    lastupdate = models.DateTimeField(blank=True, null=True)
    forcheckout = models.IntegerField()
    maxinitialtime = models.SmallIntegerField()
    project = models.CharField(max_length=6)
    size = models.SmallIntegerField()
    architecture = models.CharField(max_length=6)
    description = models.TextField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    basedoffrevisionid = models.IntegerField()

    class Meta:
        
        db_table = 'image'

class Subimages(models.Model):
    imagemetaid = models.ForeignKey(Imagemeta, db_column='imagemetaid', related_name="opa")
    imageid = models.ForeignKey(Image, db_column='imageid')

    class Meta:
        
        db_table = 'subimages'

class Imagerevision(models.Model):
    imageid = models.ForeignKey(Image, db_column='imageid')
    revision = models.SmallIntegerField()
    userid = models.ForeignKey(User, db_column='userid')
    datecreated = models.DateTimeField()
    deleted = models.IntegerField()
    datedeleted = models.DateTimeField(blank=True, null=True)
    production = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    imagename = models.CharField(max_length=75)
    autocaptured = models.IntegerField()

    class Meta:
        
        db_table = 'imagerevision'
        unique_together = (('imageid', 'revision'), ('production', 'imagename'),)


class Imagerevisioninfo(models.Model):
    imagerevisionid = models.OneToOneField(Imagerevision, db_column='imagerevisionid')
    usernames = models.CharField(max_length=512, blank=True, null=True)
    firewallenabled = models.CharField(max_length=20)
    timestamp = models.DateTimeField()

    class Meta:
        
        db_table = 'imagerevisioninfo'



class Vmtype(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        
        db_table = 'vmtype'


class Winkms(models.Model):
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')
    address = models.CharField(max_length=50)
    port = models.SmallIntegerField()

    class Meta:
        
        db_table = 'winKMS'
        unique_together = (('affiliationid', 'address'),)


class Winproductkey(models.Model):
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')
    productname = models.CharField(max_length=100)
    productkey = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'winProductKey'
        unique_together = (('affiliationid', 'productname'),)



class Connectmethod(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    connecttext = models.TextField()
    servicename = models.CharField(max_length=32)
    startupscript = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        
        db_table = 'connectmethod'
        unique_together = (('name', 'description'),)


class Connectmethodmap(models.Model):
    connectmethodid = models.ForeignKey(Connectmethod, db_column='connectmethodid')
    ostypeid = models.ForeignKey(Ostype, db_column='OStypeid', blank=True, null=True)  # Field name made lowercase.
    osid = models.ForeignKey(Os, db_column='OSid', blank=True, null=True)  # Field name made lowercase.
    imagerevisionid = models.ForeignKey(Imagerevision, db_column='imagerevisionid', blank=True, null=True)
    disabled = models.IntegerField()
    autoprovisioned = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'connectmethodmap'
        
class Connectmethodport(models.Model):
    connectmethodid = models.ForeignKey(Connectmethod, db_column='connectmethodid')
    port = models.IntegerField()
    protocol = models.CharField(max_length=3)

    class Meta:
        
        db_table = 'connectmethodport'
        unique_together = (('connectmethodid', 'port', 'protocol'),)
