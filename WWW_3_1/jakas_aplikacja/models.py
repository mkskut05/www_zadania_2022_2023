from string import octdigits
from django.db import models

# Create your models here.
class Gracz(models.Model):
    def __str__(self):
        return self.id_gracza
    id_gracza = models.IntegerField(max_length=55)
    nickname = models.CharField(max_length=55)

class Postac(models.Model):
    id_postaci = models.IntegerField(max_length=55)
    hp = models.IntegerField(max_length=1000)