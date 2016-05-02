from django.contrib import admin

# Register your models here.
from logs.models import (Log,
                        Sublog,
                        Loginlog,
                        Querylog,
                        Connectlog,
                        Computerloadlog,
                        Changelog,
                        Xmlrpclog,
                        Natlog)

admin.site.register([Log,
                    Sublog,
                    Loginlog,
                    Querylog,
                    Connectlog,
                    Computerloadlog,
                    Changelog,
                    Xmlrpclog,
                    Natlog])