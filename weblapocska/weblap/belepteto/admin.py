from django.contrib import admin

# Register your models here.

from .models import Kutyak, Felhasznalo

admin.site.register(Kutyak)
admin.site.register(Felhasznalo)