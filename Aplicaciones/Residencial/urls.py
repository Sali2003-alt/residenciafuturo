from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # UBICACIONES
    path('nuevaUbicacion/', views.nuevaUbicacion, name='nuevaUbicacion'),
    path('guardarUbicacion/', views.guardarUbicacion, name='guardarUbicacion'),
    path('listadoUbicacion/', views.listadoUbicacion, name='listadoUbicacion'),
    path('eliminarUbicacion/<int:id>/', views.eliminarUbicacion, name='eliminarUbicacion'),
    path('editarUbicacion/<int:id>/', views.editarUbicacion, name='editarUbicacion'),
    path('procesarEdicionUbicacion/', views.procesarEdicionUbicacion, name='procesarEdicionUbicacion'),


    path('nuevoProyecto/', views.nuevoProyecto, name='nuevoProyecto'),
    path('guardarProyecto/', views.guardarProyecto, name='guardarProyecto'),
    path('listadoProyecto/', views.listadoProyecto, name='listadoProyecto'),
    path('eliminarProyecto/<int:id>/', views.eliminarProyecto, name='eliminarProyecto'),
    path('editarProyecto/<int:id>/', views.editarProyecto, name='editarProyecto'),
    path('procesarEdicionProyecto/', views.procesarEdicionProyecto, name='procesarEdicionProyecto'),

# PRESUPUESTO
    path('nuevoPresupuesto/', views.nuevoPresupuesto, name='nuevoPresupuesto'),
    path('guardarPresupuesto/', views.guardarPresupuesto, name='guardarPresupuesto'),
    path('listadoPresupuesto/', views.listadoPresupuesto, name='listadoPresupuesto'),
    path('eliminarPresupuesto/<int:id>/', views.eliminarPresupuesto, name='eliminarPresupuesto'),
    path('editarPresupuesto/<int:id>/', views.editarPresupuesto, name='editarPresupuesto'),
    path('procesarEdicionPresupuesto/', views.procesarEdicionPresupuesto, name='procesarEdicionPresupuesto'),
    path('reporte_presupuestos/', views.reporte_presupuestos, name='reporte_presupuestos'),

    path('nuevoPermiso/', views.nuevoPermiso, name='nuevoPermiso'),
    path('guardarPermiso/', views.guardarPermiso, name='guardarPermiso'),
    path('listadoPermiso/', views.listadoPermiso, name='listadoPermiso'),
    path('eliminarPermiso/<int:id>/', views.eliminarPermiso, name='eliminarPermiso'),
    path('editarPermiso/<int:id>/', views.editarPermiso, name='editarPermiso'),
    path('procesarEdicionPermiso/', views.procesarEdicionPermiso, name='procesarEdicionPermiso'),


]

