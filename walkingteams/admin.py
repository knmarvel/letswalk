from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from walkingteams.models import MyUser, Team

class MyUserAdmin(UserAdmin):
    list_display = ('username', 'display_name', 'is_staff', 'is_active', 'slug',)
    list_filter = ('username', 'display_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    prepopulated_fields = {"slug": ("username",)}


class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Team, TeamAdmin)
