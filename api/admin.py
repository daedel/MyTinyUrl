from django.contrib import admin

from api.models import TinyUrl


# Register your models here.
class TinyUrlAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "url")


admin.site.register(TinyUrl)
