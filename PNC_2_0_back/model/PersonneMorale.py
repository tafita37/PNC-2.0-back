from django.db import models
from model.FormeJuridique import FormeJuridique
from model.Activite import Activite
from model.RaisonSociale import RaisonSociale
from model.Ville import Ville

class PersonneMorale(models.Model):
    id_personne_morale = models.AutoField(primary_key=True)
    nif = models.TextField(unique=True)
    date_nif = models.DateField()
    id_ville_nif = models.ForeignKey(Ville, models.DO_NOTHING, db_column='id_ville_nif', blank=True, null=True)
    id_raison_sociale = models.ForeignKey(RaisonSociale, models.DO_NOTHING, db_column='id_raison_sociale', blank=True, null=True)
    nom_commercial = models.TextField(unique=True)
    id_forme_juridique = models.ForeignKey(FormeJuridique, models.DO_NOTHING, db_column='id_forme_juridique', blank=True, null=True)
    id_activite = models.ForeignKey(Activite, models.DO_NOTHING, db_column='id_activite', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_morale'