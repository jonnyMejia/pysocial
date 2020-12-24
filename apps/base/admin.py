# Django Library
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

# Localfolder Library
from .models import (
    PyUser, PyPublication, PyComment)

class UserAdmin(UserAdmin):
    """ Admin for Users
    """
    search_fields = ( 'email',)
    list_filter = ('is_active',)
    list_display = ('__str__', 'email', 'gender', 'avatar', 'day_of_birth', )
    # list_select_related = ()
    show_full_result_count = False
    actions_selection_counter = False
    ordering = ('id',)
    # Definir fieldsets ya que "username" se establece por defecto y no debe ir
    fieldsets =  (
        (None, {'fields': ('email','password',)}),
        ('Informacion Personal', {'fields': ('first_name','last_name', 'gender', )}),
        ('Profile', {'fields': ('avatar','day_of_birth')}),
        ('Permisos', {'fields': ('is_active','is_staff','is_superuser','user_permissions',)}),
    )


admin.site.register(PyUser, UserAdmin)
admin.site.register(PyPublication)
admin.site.register(PyComment)
#admin.site.register(PyPublication, PublicationAdmin)
admin.site.register(LogEntry)