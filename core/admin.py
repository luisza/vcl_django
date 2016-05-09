from django.contrib import admin

# Register your models here.
from core.models import (Imtype,
                        State,
                        Platform,
                        Module,
                        Vmtype,
                        Osinstalltype,
                        Affiliation,
                        Variable,
                        Continuations,
                        Adminlevel,
                        Documentation,
                        Sitemaintenance)

admin.site.register([Imtype,
                    State,
                    Platform,
                    Module,
                    Osinstalltype,
                    Affiliation,
                    Vmtype,
                    Variable,
                    Continuations,
                    Adminlevel,
                    Documentation,
                    Sitemaintenance])
