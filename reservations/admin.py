from django.contrib import admin

# Register your models here.
from reservations.models import (Request,
                                Serverrequest,
                                Reservation,
                                Reservationaccounts)

admin.site.register([Request,
                        Serverrequest,
                        Reservation,
                        Reservationaccounts])