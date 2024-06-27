from django.db import models

class BureauVerbalisateur(models.Model):
    id_bureau_verbalisateur = models.AutoField(primary_key=True)
    nom_bureau_verbalisateur = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'bureau_verbalisateur'