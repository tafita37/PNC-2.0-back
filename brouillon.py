# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import connection


class Activite(models.Model):
    id_activite = models.AutoField(primary_key=True)
    nom_activite = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'activite'


class BureauVerbalisateur(models.Model):
    id_bureau_verbalisateur = models.AutoField(primary_key=True)
    nom_bureau_verbalisateur = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'bureau_verbalisateur'


class DossierMorale(models.Model):
    id_dossier_morale = models.AutoField(primary_key=True)
    id_personne_morale = models.ForeignKey('PersonneMorale', models.DO_NOTHING, db_column='id_personne_morale', blank=True, null=True)
    numero_dossier = models.TextField(unique=True)
    date_dossier = models.DateField()
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)
    numero_proces_verbal = models.TextField(unique=True)
    date_proces = models.DateField()
    id_inculpation_infraction = models.ForeignKey('InculpationInfraction', models.DO_NOTHING, db_column='id_inculpation_infraction', blank=True, null=True)
    detail_infraction = models.TextField()
    id_village = models.ForeignKey('Village', models.DO_NOTHING, db_column='id_village', blank=True, null=True)
    date_infraction = models.DateField()
    autre_information = models.TextField()
    date_cloture = models.DateField()
    id_bureau_verbalisateur = models.ForeignKey(BureauVerbalisateur, models.DO_NOTHING, db_column='id_bureau_verbalisateur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dossier_morale'


class DossierPhysique(models.Model):
    id_dossier_physique = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey('PersonnePhysique', models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    numero_dossier = models.TextField(unique=True)
    date_dossier = models.DateField()
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)
    numero_proces_verbal = models.TextField(unique=True)
    date_proces = models.DateField()
    id_inculpation_infraction = models.ForeignKey('InculpationInfraction', models.DO_NOTHING, db_column='id_inculpation_infraction', blank=True, null=True)
    detail_infraction = models.TextField()
    id_village = models.ForeignKey('Village', models.DO_NOTHING, db_column='id_village', blank=True, null=True)
    date_infraction = models.DateField()
    autre_information = models.TextField()
    date_cloture = models.DateField(blank=True, null=True)
    id_bureau_verbalisateur = models.ForeignKey(BureauVerbalisateur, models.DO_NOTHING, db_column='id_bureau_verbalisateur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dossier_physique'

class Entite(models.Model):
    id_entite = models.AutoField(primary_key=True)
    nom_entite = models.CharField(unique=True, max_length=30)
    code_entite = models.CharField(unique=True, max_length=3)
    email_entite = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'entite'
    
    


class FormeJuridique(models.Model):
    id_forme_juridique = models.AutoField(primary_key=True)
    nom_forme_juridique = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'forme_juridique'


class Inculpation(models.Model):
    id_inculpation = models.AutoField(primary_key=True)
    nom_inculpation = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'inculpation'


class InculpationInfraction(models.Model):
    id_inculpation_infraction = models.AutoField(primary_key=True)
    id_inculpation = models.ForeignKey(Inculpation, models.DO_NOTHING, db_column='id_inculpation', blank=True, null=True)
    id_infraction = models.ForeignKey('Infraction', models.DO_NOTHING, db_column='id_infraction', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inculpation_infraction'


class Infraction(models.Model):
    id_infraction = models.AutoField(primary_key=True)
    nom_infraction = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'infraction'


class Metier(models.Model):
    id_metier = models.AutoField(primary_key=True)
    nom_metier = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'metier'


class Pays(models.Model):
    id_pays = models.AutoField(primary_key=True)
    nom_pays = models.CharField(unique=True, max_length=30)
    appelation = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'pays'


class PersonneMarqueParticuliere(models.Model):
    id_personne_marque_particuliere = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey('PersonnePhysique', models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    marque = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_marque_particuliere'


class PersonneMetier(models.Model):
    id_personne_metier = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey('PersonnePhysique', models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    id_metier = models.ForeignKey(Metier, models.DO_NOTHING, db_column='id_metier', blank=True, null=True)
    date_debut_metier = models.DateField(unique=True)
    date_fin_metier = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_metier'


class PersonneMorale(models.Model):
    id_personne_morale = models.AutoField(primary_key=True)
    nif = models.TextField(unique=True)
    date_nif = models.DateField()
    id_ville_nif = models.ForeignKey('Ville', models.DO_NOTHING, db_column='id_ville_nif', blank=True, null=True)
    id_raison_sociale = models.ForeignKey('RaisonSociale', models.DO_NOTHING, db_column='id_raison_sociale', blank=True, null=True)
    nom_commercial = models.TextField(unique=True)
    id_forme_juridique = models.ForeignKey(FormeJuridique, models.DO_NOTHING, db_column='id_forme_juridique', blank=True, null=True)
    id_activite = models.ForeignKey(Activite, models.DO_NOTHING, db_column='id_activite', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_morale'


class PersonneMoraleGerant(models.Model):
    id_personne_morale_gerant = models.AutoField(primary_key=True)
    id_personne_morale = models.ForeignKey(PersonneMorale, models.DO_NOTHING, db_column='id_personne_morale', blank=True, null=True)
    id_gerant = models.ForeignKey('PersonnePhysique', models.DO_NOTHING, db_column='id_gerant', blank=True, null=True)
    id_personne_metier = models.ForeignKey(PersonneMetier, models.DO_NOTHING, db_column='id_personne_metier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_morale_gerant'


class PersonneNationalite(models.Model):
    id_personne_nationalite = models.AutoField(primary_key=True)
    id_personne_physique = models.ForeignKey('PersonnePhysique', models.DO_NOTHING, db_column='id_personne_physique', blank=True, null=True)
    id_pays = models.ForeignKey(Pays, models.DO_NOTHING, db_column='id_pays', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_nationalite'


class PersonnePhysique(models.Model):
    id_personne_physique = models.AutoField(primary_key=True)
    nom_personne_physique = models.CharField(max_length=30)
    prenom_personne_physique = models.CharField(max_length=30)
    date_naissance = models.DateField()
    numero_cin = models.TextField(unique=True)
    date_cin = models.DateField()
    id_village_cin = models.ForeignKey('Village', models.DO_NOTHING, db_column='id_village_cin', blank=True, null=True)
    sexe = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    telephone_personne_physique = models.TextField(unique=True)
    email_personne_physique = models.TextField(unique=True)
    adresse = models.TextField()

    class Meta:
        managed = False
        db_table = 'personne_physique'


class PersonnePhysiqueRelation(models.Model):
    id_personne_physique_relation = models.AutoField(primary_key=True)
    id_parent = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_parent', blank=True, null=True)
    id_enfant = models.ForeignKey(PersonnePhysique, models.DO_NOTHING, db_column='id_enfant', related_name='personnephysiquerelation_id_enfant_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personne_physique_relation'


class Profil(models.Model):
    id_profil = models.AutoField(primary_key=True)
    nom_profil = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'profil'


class RaisonSociale(models.Model):
    id_raison_sociale = models.AutoField(primary_key=True)
    nom_raison_sociale = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'raison_sociale'


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nom_region = models.CharField(unique=True, max_length=30)
    id_pays = models.ForeignKey(Pays, models.DO_NOTHING, db_column='id_pays', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    id_entite = models.ForeignKey(Entite, models.DO_NOTHING, db_column='id_entite')
    id_profil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='id_profil', blank=True, null=True)
    titre = models.CharField(max_length=30)
    nom_utilisateur = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mdp = models.TextField()

    class Meta:
        managed = False
        db_table = 'utilisateur'


class Village(models.Model):
    id_village = models.AutoField(primary_key=True)
    nom_village = models.CharField(unique=True, max_length=30)
    id_ville = models.ForeignKey('Ville', models.DO_NOTHING, db_column='id_ville', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'


class Ville(models.Model):
    id_ville = models.AutoField(primary_key=True)
    nom_ville = models.CharField(unique=True, max_length=30)
    id_region = models.ForeignKey(Region, models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ville'
