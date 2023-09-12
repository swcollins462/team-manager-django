from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'jersey_num', 'position')


admin.site.register(Player, PlayerAdmin)
