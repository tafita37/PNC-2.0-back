create database pnc;
\c pnc;

create table entite(
    id_entite serial primary key, 
    nom_entite varchar(30) unique not null, 
    code_entite varchar(3) unique not null, 
    email_entite varchar(30) unique not null
);

create table  profil(
    id_profil serial primary key, 
    nom_profil varchar(30) unique not null
);

create table utilisateur(
    id serial primary key, 
    id_entite int references entite(id_entite) not null, 
    id_profil int references profil(id_profil), 
    titre varchar(30) not null, 
    nom_utilisateur varchar(30) not null, 
    prenom varchar(30) not null, 
    email varchar(30) not null, 
    password text not null
);

create table inculpation(
    id_inculpation serial primary key, 
    nom_inculpation varchar(30) unique not null
);

create table infraction(
    id_infraction serial primary key, 
    nom_infraction varchar(30) unique not null
);

create table inculpation_infraction(
    id_inculpation_infraction serial primary key, 
    id_inculpation int references inculpation(id_inculpation), 
    id_infraction int references infraction(id_infraction)
);

create table pays(
    id_pays serial primary key, 
    nom_pays varchar(30) unique not null, 
    appelation varchar(30) unique not null
);

create table region(
    id_region serial primary key, 
    nom_region varchar(30) unique not null, 
    id_pays int references pays(id_pays)
);

create table ville(
    id_ville serial primary key, 
    nom_ville varchar(30) unique not null, 
    id_region int references region(id_region)
);

create table village(
    id_village serial primary key, 
    nom_village varchar(30) unique not null, 
    id_ville int references ville(id_ville)
);

create table bureau_verbalisateur(
    id_bureau_verbalisateur serial primary key, 
    nom_bureau_verbalisateur varchar(30) unique not null
);

create table raison_sociale(
    id_raison_sociale serial primary key, 
    nom_raison_sociale varchar(30) unique not null
);

create table forme_juridique(
    id_forme_juridique serial primary key, 
    nom_forme_juridique varchar(30) unique not null
);

create table activite(
    id_activite serial primary key, 
    nom_activite varchar(30) unique not null
);

create table metier(
    id_metier serial primary key, 
    nom_metier varchar(30) unique not null
);

create table personne_physique(
    id_personne_physique serial primary key, 
    nom_personne_physique varchar(30) not null, 
    prenom_personne_physique varchar(30) not null, 
    date_naissance date not null, 
    numero_cin text unique not null, 
    date_cin date not null, 
    id_village_cin int references village(id_village), 
    sexe int, 
    photo text, 
    telephone_personne_physique text unique not null, 
    email_personne_physique text unique not null, 
    adresse text not null
);

create table personne_physique_relation(
    id_personne_physique_relation serial primary key, 
    id_parent int references personne_physique(id_personne_physique), 
    id_enfant int references personne_physique(id_personne_physique)
);

create table personne_nationalite(
    id_personne_nationalite serial primary key, 
    id_personne_physique int references personne_physique(id_personne_physique), 
    id_pays int references pays(id_pays)
);

create table personne_metier(
    id_personne_metier serial primary key,
    id_personne_physique int references personne_physique(id_personne_physique), 
    id_metier int references metier(id_metier),
    date_debut_metier date not null unique,
    date_fin_metier date
);

create table personne_morale(
    id_personne_morale serial primary key, 
    nif text unique not null, 
    date_nif date not null, 
    id_ville_nif int references ville(id_ville),
    id_raison_sociale int references raison_sociale(id_raison_sociale), 
    nom_commercial text unique not null, 
    id_forme_juridique int references forme_juridique(id_forme_juridique), 
    id_activite int references activite(id_activite)
);

create table personne_marque_particuliere(
    id_personne_marque_particuliere serial primary key,
    id_personne_physique int references personne_physique(id_personne_physique), 
    marque text
);

create table personne_morale_gerant(
    id_personne_morale_gerant serial primary key, 
    id_personne_morale int references personne_morale(id_personne_morale), 
    id_gerant int references personne_physique(id_personne_physique), 
    id_personne_metier int references personne_metier(id_personne_metier)
);

create table dossier_morale(
    id_dossier_morale serial primary key, 
    id_personne_morale int references personne_morale(id_personne_morale), 
    numero_dossier text unique not null, 
    date_dossier date not null, 
    id_region int references region(id_region), 
    numero_proces_verbal text unique not null, 
    date_proces date not null, 
    id_inculpation_infraction int references inculpation_infraction(id_inculpation_infraction), 
    detail_infraction text not null, 
    id_village int references village(id_village), 
    date_infraction date not null, 
    autre_information text not null, 
    date_cloture date not null, 
    id_bureau_verbalisateur int references bureau_verbalisateur(id_bureau_verbalisateur)
);

create table dossier_physique(
    id_dossier_physique serial primary key, 
    id_personne_physique int references personne_physique(id_personne_physique),
    numero_dossier text unique not null, 
    date_dossier date not null, 
    id_region int references region(id_region), 
    numero_proces_verbal text unique not null, 
    date_proces date not null, 
    id_inculpation_infraction int references inculpation_infraction(id_inculpation_infraction), 
    detail_infraction text not null, 
    id_village int references village(id_village), 
    date_infraction date not null,
    autre_information text not null, 
    date_cloture date,  
    id_bureau_verbalisateur int references bureau_verbalisateur(id_bureau_verbalisateur)
);