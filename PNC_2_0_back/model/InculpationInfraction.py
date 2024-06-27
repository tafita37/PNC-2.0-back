from django.db import models
from Inculpation import *
from Infraction import *

class InculpationInfraction(models.Model):
    id_inculpation_infraction = models.AutoField(primary_key=True)
    id_inculpation = models.ForeignKey(Inculpation, models.DO_NOTHING, db_column='id_inculpation', blank=True, null=True)
    id_infraction = models.ForeignKey(Infraction, models.DO_NOTHING, db_column='id_infraction', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inculpation_infraction'