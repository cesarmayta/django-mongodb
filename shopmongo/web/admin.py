from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Producto)