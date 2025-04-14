# DnD_database

* a faire:
    - changer les types
    - lier les tables (fait?)
    - get with either name or id
    - lier les tables dans fastapi



* problems:



* questions:
    - character.attribut = liste -> comment ça marche?
    - mettre des images?


Lancer le programme:
commandes dans le terminal:
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    echo "*" > .venv/.gitignore
    pip install sqlmodel
    pip install fastapi uvicorn sqlmodel[asyncio] sqlalchemy aiosqlite
    uvicorn main:app 
ajouter /docs à la fin de l'url de la page de preview

if need to recharge preview (modifications in the code f.e.):
    pkill -f uvicorn
    uvicorn main:app