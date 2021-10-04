from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conversation)
class Conversation(admin.ModelAdmin):

    """Conversation Admin Definition"""

    list_display = ("__str__", "message_count", "participant_count")
