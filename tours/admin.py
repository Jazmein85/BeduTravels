from django.contrib import admin
from tours.models import User
from tours.models import Zona
from tours.models import Tour
from tours.models import Salida
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "email")

class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "type", "description", "zonaSalida", "zonaLlegada")

class SalidaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "fechaInicio", "fechaFin", "asientos", "precio",
        "tour")

admin.site.register(User, UserAdmin)
admin.site.register(Zona)
admin.site.register(Tour, TourAdmin)
admin.site.register(Salida, SalidaAdmin)


