from django.contrib import admin

# Register your models here.
from reservations.models import (Request,
                                Serverrequest,
                                Reservation,
                                Reservationaccounts,
                                Blockrequest,
                                Blocktimes,
                                Blockcomputers,
                                Blockwebdate,
                                Blockwebtime,)

admin.site.register([Request,
                        Serverrequest,
                        Reservation,
                        Reservationaccounts,
                        Blockrequest,
                        Blocktimes,
                        Blockcomputers,
                        Blockwebdate,
                        Blockwebtime,])