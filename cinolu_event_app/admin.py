from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class EvenementAdmin(admin.ModelAdmin):
    list_display=("id","nom_complet","numero_tel","participant","a_participe")

admin.site.register(L_impact,EvenementAdmin)

