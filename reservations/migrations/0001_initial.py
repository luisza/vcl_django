# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('authentication', '0001_initial'),
        ('compute', '0001_initial'),
        ('managementnode', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logid', models.IntegerField()),
                ('forimaging', models.IntegerField()),
                ('test', models.IntegerField()),
                ('preload', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('daterequested', models.DateTimeField()),
                ('datemodified', models.DateTimeField(blank=True, null=True)),
                ('checkuser', models.IntegerField()),
                ('laststateid', models.ForeignKey(db_column='laststateid', on_delete=django.db.models.deletion.CASCADE, related_name='rel_laststateid', to='core.State')),
                ('stateid', models.ForeignKey(db_column='stateid', on_delete=django.db.models.deletion.CASCADE, related_name='rel_si', to='core.State')),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to='authentication.User')),
            ],
            options={
                'db_table': 'request',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remoteip', models.CharField(blank=True, db_column='remoteIP', max_length=15, null=True)),
                ('lastcheck', models.DateTimeField(blank=True, null=True)),
                ('pw', models.CharField(blank=True, max_length=40, null=True)),
                ('connectip', models.CharField(blank=True, db_column='connectIP', max_length=15, null=True)),
                ('connectport', models.SmallIntegerField(blank=True, null=True)),
                ('computerid', models.ForeignKey(db_column='computerid', on_delete=django.db.models.deletion.CASCADE, to='compute.Computer')),
                ('imageid', models.ForeignKey(db_column='imageid', on_delete=django.db.models.deletion.CASCADE, to='image.Image')),
                ('imagerevisionid', models.ForeignKey(db_column='imagerevisionid', on_delete=django.db.models.deletion.CASCADE, to='image.Imagerevision')),
                ('managementnodeid', models.ForeignKey(db_column='managementnodeid', on_delete=django.db.models.deletion.CASCADE, to='managementnode.Managementnode')),
                ('requestid', models.ForeignKey(db_column='requestid', on_delete=django.db.models.deletion.CASCADE, to='reservations.Request')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='Reservationaccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('reservationid', models.ForeignKey(db_column='reservationid', on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to='authentication.User')),
            ],
            options={
                'db_table': 'reservationaccounts',
            },
        ),
        migrations.CreateModel(
            name='Serverrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serverprofileid', models.SmallIntegerField()),
                ('fixedip', models.CharField(blank=True, db_column='fixedIP', max_length=15, null=True)),
                ('fixedmac', models.CharField(blank=True, db_column='fixedMAC', max_length=17, null=True)),
                ('monitored', models.IntegerField()),
                ('admingroupid', models.ForeignKey(blank=True, db_column='admingroupid', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_agi', to='authentication.Usergroup')),
                ('logingroupid', models.ForeignKey(blank=True, db_column='logingroupid', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_login', to='authentication.Usergroup')),
                ('requestid', models.OneToOneField(db_column='requestid', on_delete=django.db.models.deletion.CASCADE, to='reservations.Request')),
            ],
            options={
                'db_table': 'serverrequest',
            },
        ),
        migrations.AlterUniqueTogether(
            name='reservationaccounts',
            unique_together=set([('reservationid', 'userid')]),
        ),
    ]
