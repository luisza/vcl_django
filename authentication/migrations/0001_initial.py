# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shibauth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField()),
                ('sessid', models.CharField(max_length=80)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'shibauth',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, null=True, unique=True)),
                ('unityid', models.CharField(max_length=80)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=25)),
                ('preferredname', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.CharField(max_length=80)),
                ('emailnotices', models.IntegerField()),
                ('imid', models.CharField(blank=True, db_column='IMid', max_length=80, null=True)),
                ('adminlevelid', models.IntegerField()),
                ('width', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('bpp', models.IntegerField()),
                ('audiomode', models.CharField(max_length=5)),
                ('mapdrives', models.IntegerField()),
                ('mapprinters', models.IntegerField()),
                ('mapserial', models.IntegerField()),
                ('rdpport', models.SmallIntegerField(blank=True, null=True)),
                ('showallgroups', models.IntegerField()),
                ('lastupdated', models.DateTimeField()),
                ('validated', models.IntegerField()),
                ('usepublickeys', models.IntegerField()),
                ('sshpublickeys', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Usergroup',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('custom', models.IntegerField()),
                ('courseroll', models.IntegerField()),
                ('initialmaxtime', models.SmallIntegerField()),
                ('totalmaxtime', models.SmallIntegerField()),
                ('maxextendtime', models.SmallIntegerField()),
                ('overlaprescount', models.SmallIntegerField(db_column='overlapResCount')),
                ('affiliationid', models.ForeignKey(blank=True, db_column='affiliationid', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Affiliation')),
                ('editusergroupid', models.ForeignKey(blank=True, db_column='editusergroupid', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Usergroup')),
            ],
            options={
                'db_table': 'usergroup',
            },
        ),
        migrations.CreateModel(
            name='Usergroupmembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usergroupid', models.ForeignKey(db_column='usergroupid', on_delete=django.db.models.deletion.CASCADE, to='authentication.Usergroup')),
            ],
            options={
                'db_table': 'usergroupmembers',
            },
        ),
        migrations.CreateModel(
            name='Usergrouppriv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usergroupid', models.ForeignKey(db_column='usergroupid', on_delete=django.db.models.deletion.CASCADE, to='authentication.Usergroup')),
            ],
            options={
                'db_table': 'usergrouppriv',
            },
        ),
        migrations.CreateModel(
            name='Usergroupprivtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('help', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usergroupprivtype',
            },
        ),
        migrations.CreateModel(
            name='Userpriv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privnodeid', models.ForeignKey(db_column='privnodeid', on_delete=django.db.models.deletion.CASCADE, to='core.Privnode')),
                ('usergroupid', models.ForeignKey(blank=True, db_column='usergroupid', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Usergroup')),
            ],
            options={
                'db_table': 'userpriv',
            },
        ),
        migrations.CreateModel(
            name='Userprivtype',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'userprivtype',
            },
        ),
        migrations.CreateModel(
            name='Localauth',
            fields=[
                ('userid', models.OneToOneField(db_column='userid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.User')),
                ('passhash', models.CharField(max_length=40)),
                ('salt', models.CharField(max_length=8)),
                ('lastupdated', models.DateTimeField()),
                ('lockedout', models.IntegerField()),
            ],
            options={
                'db_table': 'localauth',
            },
        ),
        migrations.AddField(
            model_name='userpriv',
            name='userid',
            field=models.ForeignKey(blank=True, db_column='userid', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
        migrations.AddField(
            model_name='userpriv',
            name='userprivtypeid',
            field=models.ForeignKey(db_column='userprivtypeid', on_delete=django.db.models.deletion.CASCADE, to='authentication.Userprivtype'),
        ),
        migrations.AddField(
            model_name='usergrouppriv',
            name='userprivtypeid',
            field=models.ForeignKey(db_column='userprivtypeid', on_delete=django.db.models.deletion.CASCADE, to='authentication.Usergroupprivtype'),
        ),
        migrations.AddField(
            model_name='usergroupmembers',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='ownerid',
            field=models.ForeignKey(blank=True, db_column='ownerid', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='affiliationid',
            field=models.ForeignKey(db_column='affiliationid', on_delete=django.db.models.deletion.CASCADE, to='core.Affiliation'),
        ),
        migrations.AddField(
            model_name='user',
            name='imtypeid',
            field=models.ForeignKey(db_column='IMtypeid', on_delete=django.db.models.deletion.CASCADE, to='core.Imtype'),
        ),
        migrations.AddField(
            model_name='shibauth',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
        migrations.AlterUniqueTogether(
            name='userpriv',
            unique_together=set([('userid', 'privnodeid', 'userprivtypeid')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergrouppriv',
            unique_together=set([('usergroupid', 'userprivtypeid')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergroupmembers',
            unique_together=set([('userid', 'usergroupid')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergroup',
            unique_together=set([('name', 'affiliationid')]),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('unityid', 'affiliationid')]),
        ),
    ]
