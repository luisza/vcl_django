from django.contrib import admin

# Register your models here.

from provisioning.models import (Provisioning,
                                    Provisioningosinstalltype,
                                    Resourcetype,
                                    Resource,
                                    Resourcegroup,
                                    Resourcegroupmembers,
                                    Resourcemap,
                                    Statgraphcache)

admin.site.register([Provisioning,
                        Provisioningosinstalltype,
                        Resourcetype,
                        Resource,
                        Resourcegroup,
                        Resourcegroupmembers,
                        Resourcemap,
                        Statgraphcache])