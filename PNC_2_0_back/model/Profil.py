from django.db import models

class Profil(models.Model):
    id_profil = models.AutoField(primary_key=True)
    nom_profil = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'profil'
