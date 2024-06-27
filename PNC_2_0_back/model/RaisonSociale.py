from django.db import models

class RaisonSociale(models.Model):
    id_raison_sociale = models.AutoField(primary_key=True)
    nom_raison_sociale = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'raison_sociale'