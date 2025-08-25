from .models import Tarea, Subtarea

#def recupera_tareas_y_sub_tareas():


def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)

    tarea.save()
    return tarea


#def crear_sub_tarea():


#def elimina_tarea():


#def elimina_sub_tarea():


#def imprimir_en_pantalla():
