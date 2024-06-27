from django.db import models
class Activite(models.Model):
    id_activite = models.AutoField(primary_key=True)
    nom_activite = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'activite'