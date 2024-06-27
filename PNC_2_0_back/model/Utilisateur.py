from django.db import models
from ..model.Entite import Entite
from ..model.Profil import Profil


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    id_entite = models.ForeignKey(Entite, models.DO_NOTHING, db_column='id_entite')
    id_profil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='id_profil', blank=True, null=True)
    titre = models.CharField(max_length=30)
    nom_utilisateur = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.TextField()
    username=None
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta:
        # managed = False
        db_table = 'utilisateur'
        
    def test(self) :
        print(self.id_entite.nom_entite)