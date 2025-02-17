from django.contrib import admin

from . import models

# Register your models here.

class VetAdminArea(admin.AdminSite):
    """Vet Admin panel administration"""

    site_header = "Vet Site Admin Area"


vet_admin_site = VetAdminArea(name="vet_admin")

vet_admin_site.register(models.PetOwner)
vet_admin_site.register(models.Pet)
vet_admin_site.register(models.PetDate)

admin.site.register(models.PetOwner)
admin.site.register(models.Pet)
admin.site.register(models.PetDate)