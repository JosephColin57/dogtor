from django.contrib import admin

from . import models

# Register your models here.

# Panel de administracion para la app de 'blog'

class BlogAdminArea(admin.AdminSite):
    """Blog Admin panel administration"""
    site_header = "Blog Site Admin Area"

# Instanciar nuestra clase para poder utilizar
blog_admin_site = BlogAdminArea(name="blog_admin")

# Registramos modelo 'Post' en nuestro panel admin
blog_admin_site.register(models.Post)

# Registrar en el admin general del admin
admin.site.register(models.Post)

