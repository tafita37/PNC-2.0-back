from django.db import models
from model.PersonnePhysique import PersonnePhysique

class PersonneMarqueParticuliere(models.Model):
    id_personne_marque_particuliere = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    marque = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_marque_particuliere'