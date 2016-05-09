from django.contrib import admin

# Register your models here.

from compute.models import (
                            Computer,
                            Vmprofile,
                            Vmhost,
                            Computerloadstate,
                            Computerloadflow,
                            Semaphore,
                            Serverprofile,
                            Clickthroughs
                            )

admin.site.register([
                    Computer,
                    Vmprofile,
                    Vmhost,
                    Computerloadstate,
                    Computerloadflow,
                    Semaphore,
                    Serverprofile,
                    Clickthroughs
                    ])