from django.urls import path, include
from.views import *
from rest_framework import routers

# CREAMOS LAS RUTAS DEL API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)
router.register('tiposuscripcion', TipoSuscripcionViewset)
router.register('suscripcion', SuscripcionViewset)

## SE VAN A CREAR TODAS LAS URLS
urlpatterns = [
    #API
    path('api/', include(router.urls)),
    #RUTAS
    path('', index, name="index"),

    path('mantenedorad/', mantenedorad, name="mantenedorad"),
    #path('tienda/', tienda, name="tienda"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('base/', base, name="base"),
    path('addDatosPersonales/', addDatosPersonales, name="addDatosPersonales"),
    path('deleteAdultoMayor/<username>', deleteAdultoMayor, name="deleteAdultoMayor"),
    path('deleteAdultoMayorl/<username>', deleteAdultoMayorl, name="deleteAdultoMayorl"),
    path('registrar/', registrar, name="registrar"),
    path('addAdultoMayor/<username>/', addAdultoMayor, name="addAdultoMayor"),
    path('updateAdultoMayor/<id>/', updateAdultoMayor, name="updateAdultoMayor"),
    path('updateAdultoMayorl/<id>/', updateAdultoMayorl, name="updateAdultoMayorl"),
    path('buscarad/', buscarad, name='buscarad'),
    path('listadoad/', listadoad, name='listadoad'),
    path('inscripcionTalleres/',inscripcionTalleres,name='inscripcionTalleres')
]
