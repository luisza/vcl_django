# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('compute', '0001_initial'),
        ('provisioning', '0001_initial'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nathost',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('publicipaddress', models.CharField(db_column='publicIPaddress', max_length=15)),
                ('internalipaddress', models.CharField(blank=True, db_column='internalIPaddress', max_length=15, null=True)),
                ('resourceid', models.OneToOneField(db_column='resourceid', on_delete=django.db.models.deletion.CASCADE, to='provisioning.Resource')),
            ],
            options={
                'db_table': 'nathost',
            },
        ),
        migrations.CreateModel(
            name='Nathostcomputermap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computerid', models.ForeignKey(db_column='computerid', on_delete=django.db.models.deletion.CASCADE, to='compute.Computer')),
                ('nathostid', models.ForeignKey(db_column='nathostid', on_delete=django.db.models.deletion.CASCADE, to='nat.Nathost')),
            ],
            options={
                'db_table': 'nathostcomputermap',
            },
        ),
        migrations.CreateModel(
            name='Natport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicport', models.SmallIntegerField()),
                ('connectmethodportid', models.ForeignKey(db_column='connectmethodportid', on_delete=django.db.models.deletion.CASCADE, to='image.Connectmethodport')),
                ('nathostid', models.ForeignKey(db_column='nathostid', on_delete=django.db.models.deletion.CASCADE, to='nat.Nathost')),
                ('reservationid', models.ForeignKey(db_column='reservationid', on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
            ],
            options={
                'db_table': 'natport',
            },
        ),
        migrations.AlterUniqueTogether(
            name='natport',
            unique_together=set([('nathostid', 'publicport'), ('reservationid', 'connectmethodportid')]),
        ),
        migrations.AlterUniqueTogether(
            name='nathostcomputermap',
            unique_together=set([('computerid', 'nathostid')]),
        ),
    ]
