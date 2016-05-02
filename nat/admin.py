from django.contrib import admin

# Register your models here.
from nat.models import (Nathost,
                            Nathostcomputermap,
                            Natport
                            )

admin.site.register([Nathost,
                    Nathostcomputermap,
                    Natport
                    ])