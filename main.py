from sqlmodel import Session
from fastapi import FastAPI

from database import create_db_and_tables, engine
from models import Character, Player, Actions, Weapons, Game

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



def create_weapon():
    with Session(engine) as session:
        
        w_sword = Weapons(
            w_type="physical", w_name="eh", w_range=1, damage= 4, attribute="Strength", description="something something something we win"
        )

        session.add(w_sword)
        session.commit()

        session.refresh(w_sword)

        print("Created weapon:", w_sword)


@app.post("/weapon/", response_model=Weapons)
def create_weapon_user(weapon: Weapons):
    with Session(engine) as session:
        session.add(weapon)
        session.commit()
        session.refresh(weapon)
        return weapon

@app.get("/weapon/", response_model=list[Weapons])
def read_weapons(weapon):
    with Session(engine) as session:
        weapons = session.exec(select(Weapons)).all()
        return weapons

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def main():
    create_db_and_tables()
    create_weapon()
    
    read_root()
    

if __name__ == "__main__":
    main()