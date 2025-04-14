from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from fastapi import FastAPI, HTTPException, Query, Depends
from datetime import date
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
@app.patch("/characters/{character_name}", response_model=CharactersPublic)
def update_character(
    *, session: Session = Depends(get_session), character_name: str, character: CharactersUpdate):
    db_characters = session.exec(select(Characters).where(Characters.name == character_name)).first()
    if not db_characters:
        raise HTTPException(status_code=404, detail="Character not found")
    character_data = character.model_dump(exclude_unset=True)
    for key, value in character_data.items():
        setattr(db_characters, key, value)
    session.add(db_characters)
    session.commit()
    session.refresh(db_characters)
    return db_characters
@app.delete("/characters/{character_name}")
def delete_character(character_name: str):
    with Session(engine) as session:
        character = session.exec(select(Characters).where(Characters.name == character_name)).first()
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        session.delete(character)
        session.commit()
        return {"ok": True}
@app.get("/characters/", response_model=list[CharactersPublic])
def read_characters(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    characters = session.exec(select(Characters).offset(offset).limit(limit)).all()
    return characters
@app.get("/characters/{character_name}", response_model=CharactersPublic)
def read_character(*, session: Session = Depends(get_session),character_name: str):
    character = session.exec(select(Characters).where(Characters.name == character_name)).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.post("/actions/", response_model=ActionsPublic)
def create_action_user(*, session: Session = Depends(get_session), action: ActionsCreate):
    db_actions = Actions.model_validate(action)
    session.add(db_actions)
    session.commit()
    session.refresh(db_actions)
    return db_actions
@app.patch("/actions/{action_name}", response_model=ActionsPublic)
def update_action(
    *, session: Session = Depends(get_session), action_name: str, action: ActionsUpdate):
    db_actions = session.exec(select(Actions).where(Actions.name == action_name)).first()
    if not db_actions:
        raise HTTPException(status_code=404, detail="Action not found")
    action_data = action.model_dump(exclude_unset=True)
    for key, value in action_data.items():
        setattr(db_actions, key, value)
    session.add(db_actions)
    session.commit()
    session.refresh(db_actions)
    return db_actions
@app.delete("/actions/{action_name}")
def delete_action(action_name: str):
    with Session(engine) as session:
        action = session.exec(select(Actions).where(Actions.name == action_name)).first()
        if not action:
            raise HTTPException(status_code=404, detail="Action not found")
        session.delete(action)
        session.commit()
        return {"ok": True}
@app.get("/actions/", response_model=list[ActionsPublic])
def read_actions(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    actions = session.exec(select(Actions).offset(offset).limit(limit)).all()
    return actions
@app.get("/actions/{action_name}", response_model=ActionsPublic)
def read_action(*, session: Session = Depends(get_session),action_name: str):
    action = session.exec(select(Actions).where(Actions.name == action_name)).first()
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action


@app.post("/weapons/", response_model=WeaponsPublic)
def create_weapon_user(*, session: Session = Depends(get_session), weapon: WeaponsCreate):
    db_weapon = Weapons.model_validate(weapon)
    session.add(db_weapon)
    session.commit()
    session.refresh(db_weapon)
    return db_weapon
@app.patch("/weapons/{weapon_name}", response_model=WeaponsPublic)
def update_weapon(
    *, session: Session = Depends(get_session), weapon_name: str, weapon: WeaponsUpdate):
    db_weapons = session.exec(select(Weapons).where(Weapons.w_name == weapon_name)).first()
    if not db_weapons:
        raise HTTPException(status_code=404, detail="Weapon not found")
    weapon_data = weapon.model_dump(exclude_unset=True)
    for key, value in weapon_data.items():
        setattr(db_weapons, key, value)
    session.add(db_weapons)
    session.commit()
    session.refresh(db_weapons)
    return db_weapons
@app.delete("/weapons/{weapon_name}")
def delete_weapon(weapon_name: str):
    with Session(engine) as session:
        weapon = session.exec(select(Weapons).where(Weapons.w_name == weapon_name)).first()
        if not weapon:
            raise HTTPException(status_code=404, detail="Weapon not found")
        session.delete(weapon)
        session.commit()
        return {"ok": True}
@app.get("/weapons/", response_model=list[WeaponsPublic])
def read_weapons(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    weapons = session.exec(select(Weapons).offset(offset).limit(limit)).all()
    return weapons
@app.get("/weapons/{weapon_name}", response_model=WeaponsPublic)
def read_weapon(*, session: Session = Depends(get_session), weapon_name: str):
    weapon = session.exec(select(Weapons).where(Weapons.w_name == weapon_name)).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon


@app.post("/games/", response_model=GamesPublic)
def create_game_user(*, session: Session = Depends(get_session), game: GamesCreate):
    db_game = Games.model_validate(game)
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    return db_game
@app.patch("/games/{game_name}", response_model=GamesPublic)
def update_game(
    *, session: Session = Depends(get_session), game_name: str, game: GamesUpdate):
    db_game = session.exec(select(Games).where(Games.name == game_name)).first()
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    game_data = game.model_dump(exclude_unset=True)
    for key, value in game_data.items():
        setattr(db_game, key, value)
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    return db_game
@app.delete("/games/{game_name}")
def delete_game(game_name: str):
    with Session(engine) as session:
        game = session.exec(select(Games).where(Games.name == game_name)).first()
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        session.delete(game)
        session.commit()
        return {"ok": True}
@app.get("/games/", response_model=list[GamesPublic])
def read_games(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    games = session.exec(select(Games).offset(offset).limit(limit)).all()
    return games
@app.get("/games/{game_name}", response_model=GamesPublic)
def read_game(*, session: Session = Depends(get_session), game_name: str):
    game = session.exec(select(Games).where(Games.name == game_name)).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.post("/sessions/", response_model=SessionsPublic)
def create_session_user(*, session: Session = Depends(get_session), session_game: SessionsCreate):
    db_session = Sessions.model_validate(session_game)
    session.add(db_session)
    session.commit()
    session.refresh(db_session)
    return db_session
@app.patch("/sessions/{session_date}", response_model=SessionsPublic)
def update_session(
    *, session: Session = Depends(get_session), session_date: date, session_game: SessionsUpdate):
    db_session = session.exec(select(Sessions).where(Sessions.session_date == session_date)).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found")
    session_data = session_game.model_dump(exclude_unset=True)
    for key, value in session_data.items():
        setattr(db_session, key, value)
    session.add(db_session)
    session.commit()
    session.refresh(db_session)
    return db_session
@app.delete("/sessions/{session_date}")
def delete_session(session_date: date):
    with Session(engine) as session:
        session_game = session.exec(select(Sessions).where(Sessions.session_date == session_date)).first()
        if not session_game:
            raise HTTPException(status_code=404, detail="Session not found")
        session.delete(session_game)
        session.commit()
        return {"ok": True}
@app.get("/sessions/", response_model=list[SessionsPublic])
def read_sessions(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    sessions = session.exec(select(Sessions).offset(offset).limit(limit)).all()
    return sessions
@app.get("/sessions/{session_date}", response_model=SessionsPublic)
def read_session(*, session: Session = Depends(get_session), session_date: date):
    session_game = session.exec(select(Sessions).where(Sessions.session_date == session_date)).first()
    if not session_game:
        raise HTTPException(status_code=404, detail="Session not found")
    return session_game


@app.post("/players/", response_model=SessionsPublic)
def create_player_user(*, session: Session = Depends(get_session), player: PlayersCreate):
    db_player = Players.model_validate(player)
    session.add(db_player)
    session.commit()
    session.refresh(db_player)
    return db_player
@app.patch("/players/{player_name}", response_model=PlayersPublic)
def update_player(
    *, session: Session = Depends(get_session), player_name: str, player: PlayersUpdate):
    db_player = session.exec(select(Players).where(Players.name == player_name)).first()
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    player_data = player.model_dump(exclude_unset=True)
    for key, value in player_data.items():
        setattr(db_player, key, value)
    session.add(db_player)
    session.commit()
    session.refresh(db_player)
    return db_player
@app.delete("/players/{player_name}")
def delete_player(player_name: str):
    with Session(engine) as session:
        player = session.exec(select(Players).where(Players.name == player_name)).first()
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        session.delete(player)
        session.commit()
        return {"ok": True}
@app.get("/players/", response_model=list[PlayersPublic])
def read_players(*,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)):
    players = session.exec(select(Players).offset(offset).limit(limit)).all()
    return players
@app.get("/players/{player_name}", response_model=PlayersPublic)
def read_player(*, session: Session = Depends(get_session), player_name: str):
    player = session.exec(select(Players).where(Players.name == player_name)).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player





@app.get("/")
def read_root():
    return {"Welcome to the DnD database!\n Please enter '/docs' at the end of the URL."}




