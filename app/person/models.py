from django.db import models
from django.db.models.fields import CharField

class Type(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name