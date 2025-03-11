from sqlmodel import Session
from fastapi import FastAPI

from database import create_db_and_tables, engine
from models import Character, Player, Actions, Weapons, Game

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/weapon/")
def create_weapon():
    with Session(engine) as session:
        
        w_sword = Weapons(
            w_type="physical", w_range=1, damage= 4, attribute="Strength"
        )

        session.add(w_sword)
        session.commit()

        session.refresh(w_sword)

        print("Created weapon:", w_sword)


def main():
    create_db_and_tables()
    create_weapon()


if __name__ == "__main__":
    main()