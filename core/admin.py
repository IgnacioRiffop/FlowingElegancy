from django.contrib import admin
from .models import *

# Register your models here.

# DEJA EN MODO TABLA LA VISUALIZACION EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo','fecha','imagen','vigente']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo']
    list_editable = ['precio','stock','descripcion','tipo','fecha','imagen','vigente']

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['cliente','producto','cantidad','vigente']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['producto','cantidad','vigente']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['usuario','nombre','apellido','email','password']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']
    list_editable = ['nombre','apellido','email','password']

class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['cliente','suscripcion','fecha']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['suscripcion','fecha']

class TProductoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']

class TEstadoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']

class TSuscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']
    list_editable = ['precio']

class BoletaAdmin(admin.ModelAdmin):
    list_display = ['codigo','subtotal','descuento','total']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']
    list_editable = ['subtotal','descuento','total']

class CompraAdmin(admin.ModelAdmin):
    list_display = ['codigo','cliente', 'carrito','direccion','contacto','fecha','estado']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['direccion','contacto','fecha','estado']

#admin.site.register(TipoProducto,TProductoAdmin)
#admin.site.register(Producto,ProductoAdmin)
#admin.site.register(Cliente,ClienteAdmin)
#admin.site.register(Carrito, CarritoAdmin)
#admin.site.register(Compras,CompraAdmin)
#admin.site.register(TipoSuscripcion,TSuscripcionAdmin)
#admin.site.register(Suscripcion,SuscripcionAdmin)
#admin.site.register(TipoEstado,TEstadoAdmin)
#admin.site.register(Boleta,BoletaAdmin)

class AdultoAdmin(admin.ModelAdmin):
    list_display = ['rut','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido', 'direccion', 'fecha_nacimiento', 'telefono', 'correo', 'comuna','genero','id_credencial']
    list_per_page = 10
    list_editable = ['primer_nombre','segundo_nombre','primer_apellido','segundo_apellido', 'direccion', 'fecha_nacimiento', 'telefono', 'correo', 'comuna','genero','id_credencial']

admin.site.register(AdultoMayor,AdultoAdmin)

class TallerAdmin(admin.ModelAdmin):
    list_display = ['nombre','capacidad','descripcion']
    list_per_page = 10
    list_editable = ['capacidad','descripcion']

admin.site.register(Taller,TallerAdmin)

class InscripcionTallerAdmin(admin.ModelAdmin):
    list_display = ['taller','fecha_inicio','fecha_termino','instructor','sala','adulto_mayor','instructor','nota']
    list_per_page = 10
    list_editable = ['fecha_inicio','fecha_termino','instructor','sala','adulto_mayor','instructor','nota']

admin.site.register(InscripcionTaller,InscripcionTallerAdmin)