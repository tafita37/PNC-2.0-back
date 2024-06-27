from django.db import models
from model.Pays import Pays
from model.PersonnePhysique import PersonnePhysique

class PersonneNationalite(models.Model):
    id_personne_nationalite = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    id_pays = models.ForeignKey(Pays, models.DO_NOTHING, db_column='id_pays', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_nationalite'