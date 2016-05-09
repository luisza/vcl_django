from django.contrib import admin

# Register your models here.
from authentication.models import (User,
                                    Usergroup,
                                    Usergroupmembers,
                                    Shibauth,
                                    Localauth)

admin.site.register([User,
                                    Usergroup,
                                    Usergroupmembers,
                                    Shibauth,
                                    Localauth])