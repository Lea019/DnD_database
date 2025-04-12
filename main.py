from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from fastapi import FastAPI, HTTPException, Query, Depends

from database import *
from models import *

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session



@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.post("/characters/", response_model=CharactersPublic)
def create_character_user(*, session: Session = Depends(get_session), character: CharactersCreate):
    db_characters = Characters.model_validate(character)
    session.add(db_characters)
    session.commit()
    session.refresh(db_characters)
    return db_characters
@app.patch("/characters/{character_id}", response_model=CharactersPublic)
def update_character(
    *, session: Session = Depends(get_session), character_id: int, character: CharactersUpdate):
    db_characters = session.get(Characters, character_id)
    if not db_characters:
        raise HTTPException(status_code=404, detail="Character not found")
    character_data = character.model_dump(exclude_unset=True)
    for key, value in character_data.items():
        setattr(db_characters, key, value)
    session.add(db_characters)
    session.commit()
    session.refresh(db_characters)
    return db_characters


@app.post("/actions/", response_model=ActionsPublic)
def create_action_user(*, session: Session = Depends(get_session), action: ActionsCreate):
    db_actions = Actions.model_validate(action)
    session.add(db_actions)
    session.commit()
    session.refresh(db_actions)
    return db_actions
@app.patch("/actions/{action_id}", response_model=ActionsPublic)
def update_action(
    *, session: Session = Depends(get_session), action_id: int, action: ActionsUpdate
):
    db_actions = session.get(Actions, action_id)
    if not db_actions:
        raise HTTPException(status_code=404, detail="Action not found")
    action_data = action.model_dump(exclude_unset=True)
    for key, value in action_data.items():
        setattr(db_actions, key, value)
    session.add(db_actions)
    session.commit()
    session.refresh(db_actions)
    return db_actions


@app.post("/weapons/", response_model=WeaponsPublic)
def create_weapon_user(*, session: Session = Depends(get_session), weapon: WeaponsCreate):
    db_weapon = Weapons.model_validate(weapon)
    session.add(db_weapon)
    session.commit()
    session.refresh(db_weapon)
    return db_weapon


@app.post("/games/", response_model=GamesPublic)
def create_game_user(*, session: Session = Depends(get_session), game: GamesCreate):
    db_game = Games.model_validate(game)
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    return db_game


@app.post("/sessions/", response_model=SessionsPublic)
def create_session_user(*, session: Session = Depends(get_session), session_game: SessionsCreate):
    db_session = Sessions.model_validate(session_game)
    session.add(db_session)
    session.commit()
    session.refresh(db_session)
    return db_session


@app.post("/players/", response_model=SessionsPublic)
def create_player_user(*, session: Session = Depends(get_session), player: PlayersCreate):
    db_player = Players.model_validate(player)
    session.add(db_player)
    session.commit()
    session.refresh(db_player)
    return db_player


@app.get("/characters/", response_model=list[CharactersPublic])
def read_characters(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    characters = session.exec(select(Characters).offset(offset).limit(limit)).all()
    return characters
@app.get("/characters/{characters_id}", response_model=CharactersPublic)
def read_character(*, session: Session = Depends(get_session),character_id: int):
    character = session.get(CharactersPublic, characters_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.get("/actions/", response_model=list[ActionsPublic])
def read_actions(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    actions = session.exec(select(Actions).offset(offset).limit(limit)).all()
    return actions
@app.get("/actions/{action_id}", response_model=ActionsPublic)
def read_action(*, session: Session = Depends(get_session),action_id: int):
    action = session.get(Actions, action_id)
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action


@app.get("/weapons/", response_model=list[WeaponsPublic])
def read_weapons(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    weapons = session.exec(select(Weapons).offset(offset).limit(limit)).all()
    return weapons
@app.get("/weapons/{weapon_id}", response_model=WeaponsPublic)
def read_weapon(*, session: Session = Depends(get_session),weapon_id: int):
    weapon = session.get(Weapons, weapon_id)
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon


@app.get("/games/", response_model=list[GamesPublic])
def read_games(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    games = session.exec(select(Games).offset(offset).limit(limit)).all()
    return games
@app.get("/games/{game_id}", response_model=GamesPublic)
def read_game(*, session: Session = Depends(get_session),game_id: int):
    game = session.get(Games, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.get("/sessions/", response_model=list[SessionsPublic])
def read_sessions(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    sessions = session.exec(select(Sessions).offset(offset).limit(limit)).all()
    return sessions
@app.get("/sessions/{session_id}", response_model=SessionsPublic)
def read_session(*, session: Session = Depends(get_session), session_id: int):
    session_game = session.get(Sessions, session_game)
    if not session_game:
        raise HTTPException(status_code=404, detail="Session not found")
    return session_game


@app.get("/players/", response_model=list[PlayersPublic])
def read_players(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    players = session.exec(select(Players).offset(offset).limit(limit)).all()
    return players
@app.get("/players/{player_id}", response_model=PlayersPublic)
def read_player(*, session: Session = Depends(get_session), player_id: int):
    player = session.get(Players, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.get("/")
def read_root():
    return {"Welcome to the DnD database!"}




