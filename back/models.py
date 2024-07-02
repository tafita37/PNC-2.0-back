from django.db import models
from PNC_2_0_back.model.Entite import Entite
from PNC_2_0_back.model.Profil import Profil
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    entite = models.ForeignKey(Entite, models.DO_NOTHING, db_column='id_entite', blank=True, null=True)
    profil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='id_profil', blank=True, null=True)
    nomUtilisateur = models.CharField(max_length=30, db_column='nom_utilisateur')
    prenom = models.CharField(max_length=30, db_column='prenom')
    email = models.TextField(unique=True, db_column='email')
    password = models.TextField(db_column='password')
    
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