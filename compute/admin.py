from django.contrib import admin

# Register your models here.

from compute.models import (Scheduletimes,
                            Computer,
                            Vmprofile,
                            Vmhost,
                            Computerloadstate,
                            Computerloadflow,
                            Blockrequest,
                            Blocktimes,
                            Blockcomputers,
                            Blockwebdate,
                            Blockwebtime,
                            Semaphore,
                            Serverprofile,
                            Clickthroughs
                            )

admin.site.register([Scheduletimes,
                    Computer,
                    Vmprofile,
                    Vmhost,
                    Computerloadstate,
                    Computerloadflow,
                    Blockrequest,
                    Blocktimes,
                    Blockcomputers,
                    Blockwebdate,
                    Blockwebtime,
                    Semaphore,
                    Serverprofile,
                    Clickthroughs
                    ])