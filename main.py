from sqlmodel import Session

from .database import create_db_and_tables, engine
from .models import Character, Player, Actions, Weapons, Game


def create_heroes():
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
    create_heroes()


if __name__ == "__main__":
    main()