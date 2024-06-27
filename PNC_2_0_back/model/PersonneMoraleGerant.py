from django.db import models
from model.PersonneMetier import PersonneMetier
from model.PersonneMorale import PersonneMorale
from model.PersonnePhysique import PersonnePhysique

class PersonneMoraleGerant(models.Model):
    id_personne_morale_gerant = models.AutoField(primary_key=True)
    id_personne_morale = models.ForeignKey(PersonneMorale, models.DO_NOTHING, db_column='id_personne_morale', blank=True, null=True)
    id_gerant = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_gerant', blank=True, null=True)
    id_personne_metier = models.ForeignKey(PersonneMetier, models.DO_NOTHING, db_column='id_personne_metier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_morale_gerant'