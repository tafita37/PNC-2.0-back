from django.db import models
from PNC_2_0_back.model.Entite import Entite
from PNC_2_0_back.model.Profil import Profil
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    id_entite = models.ForeignKey(Entite, models.DO_NOTHING, db_column='id_entite', blank=True, null=True)
    id_profil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='id_profil', blank=True, null=True)
    nom_utilisateur = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.TextField(unique=True)
    password = models.TextField()
    
    username=None
    last_login = None
    is_superuser=None
    first_name=None
    last_name=None
    is_staff=None
    is_active=True
    date_joined=None
    mdp=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta:
        managed = False
        db_table = 'utilisateur'