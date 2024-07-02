from django.db import models

class Profil(models.Model):
    idProfil = models.AutoField(primary_key=True, db_column='id_profil')
    nomProfil = models.CharField(unique=True, max_length=30, db_column='nom_profil')

    class Meta:
        managed = False
        db_table = 'profil'
