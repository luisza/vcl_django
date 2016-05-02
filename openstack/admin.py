from django.contrib import admin

# Register your models here.

from openstack.models import Openstackcomputermap, Openstackimagerevision

admin.site.register([Openstackcomputermap,
                     Openstackimagerevision])