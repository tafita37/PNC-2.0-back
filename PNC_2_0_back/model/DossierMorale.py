from django.db import models
from model.InculpationInfraction import InculpationInfraction
from model.Region import Region
from model.BureauVerbalisateur import BureauVerbalisateur
from model.PersonneMorale import PersonneMorale
from model.Village import Village

class DossierMorale(models.Model):
    id_dossier_morale = models.AutoField(primary_key=True)
    id_personne_morale = models.ForeignKey(PersonneMorale, models.DO_NOTHING, db_column='id_personne_morale', blank=True, null=True)
    numero_dossier = models.TextField(unique=True)
    date_dossier = models.DateField()
    id_region = models.ForeignKey(Region, models.DO_NOTHING, db_column='id_region', blank=True, null=True)
    numero_proces_verbal = models.TextField(unique=True)
    date_proces = models.DateField()
    id_inculpation_infraction = models.ForeignKey(InculpationInfraction, models.DO_NOTHING, db_column='id_inculpation_infraction', blank=True, null=True)
    detail_infraction = models.TextField()
    id_village = models.ForeignKey(Village, models.DO_NOTHING, db_column='id_village', blank=True, null=True)
    date_infraction = models.DateField()
    autre_information = models.TextField()
    date_cloture = models.DateField()
    id_bureau_verbalisateur = models.ForeignKey(BureauVerbalisateur, models.DO_NOTHING, db_column='id_bureau_verbalisateur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dossier_morale'