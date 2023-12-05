from django.db import models

# Create your models here.
class Trabajo(models.Model):
    name = models.CharField(max_length=200)
    fecha = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return (self.title) + " - " + (self.project.name)