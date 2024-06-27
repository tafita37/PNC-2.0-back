from django.db import models
from model.Pays import Pays

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nom_region = models.CharField(unique=True, max_length=30)
    id_pays = models.ForeignKey(Pays, models.DO_NOTHING, db_column='id_pays', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'