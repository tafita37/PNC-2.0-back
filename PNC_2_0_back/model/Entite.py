from django.db import models

class Entite(models.Model):
    idEntite = models.AutoField(primary_key=True, db_column='id_entite')
    nomEntite = models.CharField(unique=True, max_length=30, db_column='nom_entite')
    codeEntite = models.CharField(unique=True, max_length=3, db_column='code_entite')
    emailEntite = models.CharField(unique=True, max_length=3, db_column='email_entite')

    class Meta:
        managed = False
        db_table = 'entite'