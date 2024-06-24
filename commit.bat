@echo off
setlocal

:: Mettre à jour votre branche locale avec les dernières modifications du dépôt distant
git pull origin main --allow-unrelated-histories

:: Ajouter toutes les modifications dans le répertoire de travail à l'index de Git
git add .

:: Demander à l'utilisateur d'entrer un message de commit
set /p commit_message="Entrez votre message de commit : "

:: Vérifier si le message de commit n'est pas vide
if "%commit_message%"=="" (
    echo Le message de commit ne peut pas être vide.
    exit /b 1
)

:: Faire le commit avec le message entré par l'utilisateur
git commit -m "%commit_message%"

:: Pousser les modifications vers le dépôt distant sur la branche main
git push origin main

endlocal
