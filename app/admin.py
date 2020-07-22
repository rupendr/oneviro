from django.contrib import admin
from .models import AboutTeam

# Register your models here.

class AboutTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation') 

admin.site.register(AboutTeam, AboutTeamAdmin)