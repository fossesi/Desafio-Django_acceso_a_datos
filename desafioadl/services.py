from .models import Tarea, Subtarea

def imprimir_en_pantalla(resultado):
                    
    for item in resultado:
        tarea = item["tarea"]
        print(f"[{tarea.id}] descripcion tarea: {tarea.descripcion}")
        for subtarea in item["subtareas"]:
            print(f" .... [{subtarea.id}] {subtarea.descripcion}")
  
def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    resultado = []
    for tarea in tareas:
        subtareas = Subtarea.objects.filter(tarea_id=tarea)
        resultado.append({
            "tarea": tarea,
            "subtareas": list(subtareas)
        })
    return resultado


def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)

    tarea.save()
    imprimir_en_pantalla()


def crear_sub_tarea(descripcion_subtarea, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    sub_tarea = Subtarea(descripcion=descripcion_subtarea, tarea_id=tarea)

    sub_tarea.save()
    return sub_tarea


def elimina_tarea(id):
    tarea = Tarea.objects.filter(id=id).delete()

    return tarea


def elimina_sub_tarea(sub_tarea_id):
    sub_tarea = Subtarea.objects.filter(id=sub_tarea_id).delete()

    return sub_tarea
