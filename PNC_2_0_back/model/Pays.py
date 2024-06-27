from django.db import models

class Pays(models.Model):
    id_pays = models.AutoField(primary_key=True)
    nom_pays = models.CharField(unique=True, max_length=30)
    appelation = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'pays'