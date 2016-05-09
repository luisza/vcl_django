from __future__ import unicode_literals

from django.db import models
from authentication.models import User

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
