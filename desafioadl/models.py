from django.db import models

# Create your models here.
class Tarea (models.Model):
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.descripcion} - {self.eliminada}"
    
class Subtarea (models.Model):
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name="subtareas")

    def __str__(self):
        return f"{self.tarea_id} - {self.descripcion} - {self.eliminada}"