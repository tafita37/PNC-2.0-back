from django.db import models

class Inculpation(models.Model):
    id_inculpation = models.AutoField(primary_key=True)
    nom_inculpation = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'inculpation'