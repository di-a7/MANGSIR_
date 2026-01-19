from django.db import models

# Create your models here.

class Todolist(models.Model):
   title = models.CharField(max_length=75)
   description = models.TextField()
   status = models.BooleanField()

# model_class -> migration_file -> migrate(database_tables)

