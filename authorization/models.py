from __future__ import unicode_literals

from django.db import models
from authentication.models import Usergroup, User
from core.models import Userprivtype, Usergroupprivtype
from provisioning.models import Resourcegroup

# Create your models here.

class Privnode(models.Model):
    parent = models.ForeignKey('self', db_column='parent')
    name = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'privnode'
        unique_together = (('parent', 'name'),)
        

class Userpriv(models.Model):
    #id = models.AutoField()
    userid = models.ForeignKey(User, db_column='userid', blank=True, null=True)
    usergroupid = models.ForeignKey(Usergroup, db_column='usergroupid', blank=True, null=True)
    privnodeid = models.ForeignKey(Privnode, db_column='privnodeid')
    userprivtypeid = models.ForeignKey(Userprivtype, db_column='userprivtypeid')

    class Meta:
        
        db_table = 'userpriv'
        unique_together = (('userid', 'privnodeid', 'userprivtypeid'),)

        
class Usergrouppriv(models.Model):
    usergroupid = models.ForeignKey(Usergroup, db_column='usergroupid')
    userprivtypeid = models.ForeignKey(Usergroupprivtype, db_column='userprivtypeid')

    class Meta:
        
        db_table = 'usergrouppriv'
        unique_together = (('usergroupid', 'userprivtypeid'),)
        
        
class Resourcepriv(models.Model):
    resourcegroupid = models.ForeignKey(Resourcegroup, db_column='resourcegroupid')
    privnodeid = models.ForeignKey(Privnode, db_column='privnodeid')
    type = models.CharField(max_length=13)

    class Meta:
        
        db_table = 'resourcepriv'
        unique_together = (('resourcegroupid', 'privnodeid', 'type'),)