@echo off
title Installation et lancement du bot DM All

echo ===============================
echo Mise à jour de pip et installation des packages
echo ===============================

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
if not exist ".env" (
    echo ⚠️ Fichier .env introuvable !
    echo Veuillez créer un fichier .env avec la ligne suivante :
    echo TOKEN=PASTEYOURTOKENHERE  
    pause
    exit /b 1
)

echo.
echo Démarrage du bot...
python dmall.py

pause
