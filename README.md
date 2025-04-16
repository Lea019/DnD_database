# DnD_database

## Présentation du projet
Ceci est une database conçue pour enregistrer vos données de Donjon&Dragon! Elle est accessible et instinctive. Elle est accompagnée d'une API. Liez vos personnages, joueurs, parties et sessions afin de retrouver vos informations facilement!

## Manuel de l'utilisateur:
- Commandes dans le terminal:
> python -m venv .venv
> source .venv/bin/activate
> python -m pip install --upgrade pip
> echo "*" > .venv/.gitignore
> pip install sqlmodel
> pip install fastapi uvicorn sqlmodel[asyncio] sqlalchemy aiosqlite
> python main.py
> uvicorn main:app
- Ajouter */docs* à la fin de l'url de la page de preview

*Amusez-vous bien!*

## Explication des différentes parties du projet
Les différents fichiers permettent la distinction entre les différentes parties du projet.

### models.py
Ce fichier contient la partie SQLModel du projet.

### main.py
Ce fichier contient le code de l'API programmée avec FastAPI. IL permet de lancer les autres fichiers et en importe les informations.

### database.py
Ce fichier contient le code des informations liées à la base de données: path, files. Il crée également le fichier .db de la base de données.

### database.db
Il s'agit de la base de données.

## idées d'améliorations:
- mettre des images
- donner la possibilité de selectioner par id ou name