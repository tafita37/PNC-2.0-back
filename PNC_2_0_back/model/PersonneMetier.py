from django.db import models
from model.Metier import Metier
from model.PersonnePhysique import PersonnePhysique

class PersonneMetier(models.Model):
    id_personne_metier = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    id_metier = models.ForeignKey(Metier, models.DO_NOTHING, db_column='id_metier', blank=True, null=True)
    date_debut_metier = models.DateField(unique=True)
    date_fin_metier = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_metier'