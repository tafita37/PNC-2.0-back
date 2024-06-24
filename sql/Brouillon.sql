create table general_page(
    id_general_page serial primary key, 
    nom_general_page varchar(20) unique not null, 
    contenu_general_page text not null
);

create table connexion_page(
    id_connexion_page serial primary key, 
    page_connexion_page varchar(20) unique not null, 
    url_connexion_page varchar(20) unique not null, 
    componentName varchar(30) not null
);

create table utilisateur_connexion_page(
    id_utilisateur_connexion_page serial primary key, 
    id_utilisateur int references utilisateur(id_utilisateur), 
    id_connexion_page int references connexion_page(id_connexion_page)
);
