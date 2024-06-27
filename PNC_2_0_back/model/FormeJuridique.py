from django.db import models

class FormeJuridique(models.Model):
    id_forme_juridique = models.AutoField(primary_key=True)
    nom_forme_juridique = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'forme_juridique'