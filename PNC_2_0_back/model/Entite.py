from django.db import models

class Entite(models.Model):
    id_entite = models.AutoField(primary_key=True)
    nom_entite = models.CharField(unique=True, max_length=30)
    code_entite = models.CharField(unique=True, max_length=3)
    email_entite = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'entite'