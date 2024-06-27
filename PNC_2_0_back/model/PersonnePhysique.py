from django.db import models
from model.Village import Village

class PersonnePhysique(models.Model):
    id_personne_physique = models.AutoField(primary_key=True)
    nom_personne_physique = models.CharField(max_length=30)
    prenom_personne_physique = models.CharField(max_length=30)
    date_naissance = models.DateField()
    numero_cin = models.TextField(unique=True)
    date_cin = models.DateField()
    id_village_cin = models.ForeignKey(Village, models.DO_NOTHING, db_column='id_village_cin', blank=True, null=True)
    sexe = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    telephone_personne_physique = models.TextField(unique=True)
    email_personne_physique = models.TextField(unique=True)
    adresse = models.TextField()

    class Meta:
        managed = False
        db_table = 'personne_physique'