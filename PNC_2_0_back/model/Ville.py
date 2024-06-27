from django.db import models
from model.Region import Region

class Ville(models.Model):
    id_ville = models.AutoField(primary_key=True)
    nom_ville = models.CharField(unique=True, max_length=30)
    id_region = models.ForeignKey(Region, models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ville'