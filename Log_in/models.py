from django.db import models
from datetime import datetime

# Create your models here.
from django.db.models import CharField


class Materials(models.Model):
    materials_title = models.CharField(max_length=200)
    materials_content = models.TextField()
    materials_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.materials_title