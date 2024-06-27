from django.db import models
from model.Ville import Ville

class Village(models.Model):
    id_village = models.AutoField(primary_key=True)
    nom_village = models.CharField(unique=True, max_length=30)
    id_ville = models.ForeignKey(Ville, models.DO_NOTHING, db_column='id_ville', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'