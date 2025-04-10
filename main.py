from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, HTTPException

from database import *
from models import *

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




@app.post("/characters/", response_model=list[CharactersCreate])
def create_character_user(character: CharactersCreate):
    with Session(engine) as session:
        db_characters = Characters.model_validate(character)
        session.add(db_characters)
        session.commit()
        session.refresh(db_characters)
        return db_characters

@app.post("/actions/", response_model=list[ActionsCreate])
def create_action_user(action: ActionsCreate):
    with Session(engine) as session:
        db_actions = Actions.model_validate(action)
        session.add(db_actions)
        session.commit()
        session.refresh(db_actions)
        return db_actions

@app.post("/weapons/", response_model=list[WeaponsCreate])
def create_weapon_user(weapon: WeaponsCreate):
    with Session(engine) as session:
        db_weapon = Weapons.model_validate(weapon)
        session.add(db_weapon)
        session.commit()
        session.refresh(db_weapon)
        return db_weapon

@app.post("/games/", response_model=list[GamesCreate])
def create_game_user(game: GamesCreate):
    with Session(engine) as session:
        db_games = Games.model_validate(game)
        session.add(db_games)
        session.commit()
        session.refresh(db_games)
        return db_games

@app.post("/players/", response_model=list[PlayersCreate])
def create_player_user(player: PlayersCreate):
    with Session(engine) as session:
        db_players = Players.model_validate(player)
        session.add(db_players)
        session.commit()
        session.refresh(db_players)
        return db_players

@app.get("/characters/", response_model=list[CharactersPublic])
def read_characters():
    with Session(engine) as session:
        characters = session.exec(select(Characters)).all()
        return characters

@app.get("/characters/{character_id}", response_model=CharactersPublic)
def read_character(character_id: int):
    with Session(engine) as session:
        character = session.get(Characters, character_id)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return character

@app.get("/actions/", response_model=list[ActionsPublic])
def read_actions():
    with Session(engine) as session:
        actions = session.exec(select(Actions)).all()
        return actions

@app.get("/actions/{action_id}", response_model=ActionsPublic)
def read_action(action_id: int):
    with Session(engine) as session:
        action = session.get(Actions, action_id)
        if not action:
            raise HTTPException(status_code=404, detail="Action not found")
        return action

@app.get("/weapons/", response_model=list[WeaponsPublic])
def read_weapons():
    with Session(engine) as session:
        weapons = session.exec(select(Weapons)).all()
        return weapons

@app.get("/weapons/{weapon_id}", response_model=WeaponsPublic)
def read_weapon(weapon_id: int):
    with Session(engine) as session:
        weapon = session.get(Weapons, weapon_id)
        if not weapon:
            raise HTTPException(status_code=404, detail="Weapon not found")
        return weapon

@app.get("/games/", response_model=list[GamesPublic])
def read_games():
    with Session(engine) as session:
        games = session.exec(select(Games)).all()
        return games

@app.get("/games/{game_id}", response_model=GamesPublic)
def read_game(game_id: int):
    with Session(engine) as session:
        game = session.get(Games, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        return game

@app.get("/players/", response_model=list[PlayersPublic])
def read_players():
    with Session(engine) as session:
        players = session.exec(select(Players)).all()
        return players

@app.get("/players/{player_id}", response_model=PlayersPublic)
def read_player(player_id: int):
    with Session(engine) as session:
        player = session.get(Players, player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        return player

@app.get("/")
def read_root():
    return {"message": "Welcome to the DnD database!"}




