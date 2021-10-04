from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class Reservation(admin.ModelAdmin):

    """Reservation Model Definition"""

    list_display = (
        "room",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )
