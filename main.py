from sqlmodel import Session, select
from fastapi import FastAPI

from database import create_db_and_tables, engine
from models import Character, Player, Actions, Weapons, Game

app = FastAPI()




@app.on_event("startup")
def on_startup():
    create_db_and_tables()



def create_weapon():
    with Session(engine) as session:
        session.add()
        session.commit()

        session.refresh()

        print("Created weapon:", )


@app.post("/weapons/")
def create_weapon_user(weapons: Weapons):
    with Session(engine) as session:
        session.add(weapon)
        session.commit()
        session.refresh(weapon)
        return weapon

@app.get("/weapons/", response_model=list[Weapons])
def read_weapons():
    with Session(engine) as session:
        weapons = session.exec(select(Weapons)).all()
        return weapons

@app.get("/")
def read_root():
    return {"message": "Welcome to the DnD database!"}




