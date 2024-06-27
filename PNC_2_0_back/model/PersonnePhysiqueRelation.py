from django.db import models
from model.PersonnePhysique import PersonnePhysique

class PersonnePhysiqueRelation(models.Model):
    id_personne_physique_relation = models.AutoField(primary_key=True)
    id_parent = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_parent', blank=True, null=True)
    id_enfant = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_enfant', related_name='personnephysiquerelation_id_enfant_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_physique_relation'