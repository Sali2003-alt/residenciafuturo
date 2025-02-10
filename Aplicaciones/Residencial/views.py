from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ubicacion
from .models import Proyecto
from decimal import Decimal
from .models import Presupuesto
from .models import Permiso

# Función para mostrar la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Función para mostrar el formulario de nueva ubicación
def nuevaUbicacion(request):
    return render(request, 'nuevaUbicacion.html')

# Función para guardar una nueva ubicación
def guardarUbicacion(request):
    if request.method == "POST":
        direccion = request.POST['txt_direccion']
        ciudad = request.POST['txt_ciudad']
        provincia = request.POST['txt_provincia']
        pais = request.POST['txt_pais']
        codigo_postal = request.POST['txt_codigo_postal']

        # Validar que los campos no estén vacíos
        if not direccion or not ciudad or not provincia or not pais or not codigo_postal:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('/nuevaUbicacion')

        # Crear una nueva ubicación
        nueva_ubicacion = Ubicacion.objects.create(
            direccion=direccion,
            ciudad=ciudad,
            provincia=provincia,
            pais=pais,
            codigo_postal=codigo_postal
        )

        messages.success(request, "Ubicación registrada exitosamente")
        return redirect('/listadoUbicacion')

# Función para listar las ubicaciones
def listadoUbicacion(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'listadoUbicacion.html', {'ubicaciones': ubicaciones})

# Función para eliminar una ubicación
def eliminarUbicacion(request, id):
    ubicacion_eliminar = get_object_or_404(Ubicacion, id=id)
    ubicacion_eliminar.delete()
    messages.success(request, "Ubicación eliminada correctamente")
    return redirect('/listadoUbicacion')

# Función para mostrar el formulario de edición de una ubicación
def editarUbicacion(request, id):
    ubicacion_editar = get_object_or_404(Ubicacion, id=id)
    return render(request, 'editarUbicacion.html', {'ubicacion': ubicacion_editar})

# Función para procesar la edición de una ubicación
def procesarEdicionUbicacion(request):
    if request.method == "POST":
        ubicacion_id = request.POST['id']
        ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)

        # Actualizar los campos de la ubicación
        ubicacion.direccion = request.POST['txt_direccion']
        ubicacion.ciudad = request.POST['txt_ciudad']
        ubicacion.provincia = request.POST['txt_provincia']
        ubicacion.pais = request.POST['txt_pais']
        ubicacion.codigo_postal = request.POST['txt_codigo_postal']
        ubicacion.save()

        messages.success(request, "Ubicación actualizada exitosamente")
        return redirect('/listadoUbicacion')




# Vista para mostrar el formulario de nuevo proyecto
def nuevoProyecto(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'nuevoProyecto.html', {'ubicaciones': ubicaciones})

# Vista para guardar un nuevo proyecto en la base de datos
def guardarProyecto(request):
    if request.method == 'POST':
        nombre = request.POST['txt_nombre']
        descripcion = request.POST['txt_descripcion']
        fecha_inicio = request.POST['txt_fecha_inicio']
        fecha_fin = request.POST.get('txt_fecha_fin', None)
        ubicacion_id = request.POST['sel_ubicacion']
        estado = request.POST['sel_estado']

        ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)

        proyecto = Proyecto(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin if fecha_fin else None,
            ubicacion=ubicacion,
            estado=estado
        )
        proyecto.save()
        messages.success(request, "Proyecto guardado exitosamente")
        return redirect('listadoProyecto')

    return redirect('nuevoProyecto')

# Vista para mostrar la lista de proyectos
def listadoProyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'listadoProyecto.html', {'proyectos': proyectos})

# Vista para eliminar un proyecto
def eliminarProyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    messages.success(request, "Proyecto eliminado exitosamente")
    return redirect('listadoProyecto')

# Vista para mostrar el formulario de edición con datos prellenados
def editarProyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'editarProyecto.html', {'proyecto': proyecto, 'ubicaciones': ubicaciones})

# Vista para procesar la edición del proyecto
def procesarEdicionProyecto(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['txt_nombre']
        descripcion = request.POST['txt_descripcion']
        fecha_inicio = request.POST['txt_fecha_inicio']
        fecha_fin = request.POST.get('txt_fecha_fin', None)
        ubicacion_id = request.POST['sel_ubicacion']
        estado = request.POST['sel_estado']

        proyecto = get_object_or_404(Proyecto, id=id)
        proyecto.nombre = nombre
        proyecto.descripcion = descripcion
        proyecto.fecha_inicio = fecha_inicio
        proyecto.fecha_fin = fecha_fin if fecha_fin else None
        proyecto.ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)
        proyecto.estado = estado
        proyecto.save()

        messages.success(request, "Proyecto actualizado exitosamente")
        return redirect('listadoProyecto')

    return redirect('listadoProyecto')



# Función para mostrar el formulario de nuevo presupuesto
def nuevoPresupuesto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'nuevoPresupuesto.html', {'proyectos': proyectos})

# Función para guardar un nuevo presupuesto
def guardarPresupuesto(request):
    if request.method == "POST":
        proyecto_id = request.POST['proyecto']
        monto = request.POST['monto']
        descripcion = request.POST['descripcion']
        tipo = request.POST['tipo']

        # Validar que los campos requeridos no estén vacíos
        if not proyecto_id or not monto or not descripcion or not tipo:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('/nuevoPresupuesto')

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)

        # Crear un nuevo presupuesto
        nuevo_presupuesto = Presupuesto.objects.create(
            proyecto=proyecto,
            monto=Decimal(monto),
            descripcion=descripcion,
            tipo=tipo
        )

        messages.success(request, "Presupuesto registrado exitosamente")
        return redirect('/listadoPresupuesto')

# Función para listar los presupuestos
def listadoPresupuesto(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'listadoPresupuesto.html', {'presupuestos': presupuestos})

# Función para eliminar un presupuesto
def eliminarPresupuesto(request, id):
    presupuesto_eliminar = get_object_or_404(Presupuesto, id=id)
    presupuesto_eliminar.delete()
    messages.success(request, "Presupuesto eliminado correctamente")
    return redirect('/listadoPresupuesto')

# Función para mostrar el formulario de edición de un presupuesto
def editarPresupuesto(request, id):
    presupuesto_editar = get_object_or_404(Presupuesto, id=id)
    proyectos = Proyecto.objects.all()
    return render(request, 'editarPresupuesto.html', {'presupuesto': presupuesto_editar, 'proyectos': proyectos})

# Función para procesar la edición de un presupuesto
def procesarEdicionPresupuesto(request):
    if request.method == "POST":
        presupuesto_id = request.POST['id']
        presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)

        proyecto_id = request.POST['proyecto']
        monto = request.POST['monto']
        descripcion = request.POST['descripcion']
        tipo = request.POST['tipo']

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)

        # Actualizar el presupuesto
        presupuesto.proyecto = proyecto
        presupuesto.monto = Decimal(monto)
        presupuesto.descripcion = descripcion
        presupuesto.tipo = tipo
        presupuesto.save()

        messages.success(request, "Presupuesto actualizado exitosamente")
        return redirect('/listadoPresupuesto')

# Función para generar un reporte de presupuestos
def reporte_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'reporte_presupuestos.html', {'presupuestos': presupuestos})




# Vista para mostrar el formulario de nuevo permiso
def nuevoPermiso(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'nuevoPermiso.html', {'proyectos': proyectos})

# Vista para guardar un nuevo permiso
def guardarPermiso(request):
    if request.method == "POST":
        proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto'])
        tipo_permiso = request.POST['tipo_permiso']
        fecha_emision = request.POST['fecha_emision']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        estado = request.POST['estado']

        nuevo_permiso = Permiso(
            proyecto=proyecto,
            tipo_permiso=tipo_permiso,
            fecha_emision=fecha_emision,
            fecha_vencimiento=fecha_vencimiento,
            estado=estado
        )
        nuevo_permiso.save()
        messages.success(request, "Permiso guardado correctamente.")
        return redirect('listadoPermiso')

    return redirect('nuevoPermiso')

# Vista para listar los permisos
def listadoPermiso(request):
    permisos = Permiso.objects.all()
    return render(request, 'listadoPermiso.html', {'permisos': permisos})

# Vista para eliminar un permiso
def eliminarPermiso(request, id):
    permiso = get_object_or_404(Permiso, id=id)
    permiso.delete()
    messages.success(request, "Permiso eliminado correctamente.")
    return redirect('listadoPermiso')

# Vista para mostrar el formulario de edición de permiso
def editarPermiso(request, id):
    permiso = get_object_or_404(Permiso, id=id)
    proyectos = Proyecto.objects.all()
    return render(request, 'editarPermiso.html', {'permiso': permiso, 'proyectos': proyectos})

# Vista para procesar la edición de un permiso
def procesarEdicionPermiso(request):
    if request.method == "POST":
        permiso = get_object_or_404(Permiso, id=request.POST['id'])
        permiso.proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto'])
        permiso.tipo_permiso = request.POST['tipo_permiso']
        permiso.fecha_emision = request.POST['fecha_emision']
        permiso.fecha_vencimiento = request.POST['fecha_vencimiento']
        permiso.estado = request.POST['estado']
        permiso.save()

        messages.success(request, "Permiso actualizado correctamente.")
        return redirect('listadoPermiso')

    return redirect('editarPermiso', id=request.POST['id'])