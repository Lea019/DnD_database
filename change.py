@app.post("/games/{game_id}/sessions/{character_id}", status_code=201)
def add_character_to_game(
    game_id: int,
    character_id: int,
    session: Session = Depends(get_session)):
    existing = session.exec(
        select(GameCharacterLink).where(
            GameCharacterLink.game_id == game_id,
            GameCharacterLink.character_id == character_id
        )
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Character already linked to game")

    link = GameCharacterLink(game_id=game_id, character_id=character_id)
    session.add(link)
    session.commit()
    return {"message": "Character linked to game"}
@app.delete("/games/{game_id}/sessions/{character_id}", status_code=204)
def remove_character_from_game(
    game_id: int,
    character_id: int,
    session: Session = Depends(get_session)):
    link = session.exec(
        select(GameCharacterLink).where(
            GameCharacterLink.game_id == game_id,
            GameCharacterLink.character_id == character_id
        )
    ).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    session.delete(link)
    session.commit()
@app.get("/sessions/{character_id}/games", response_model=List[GamesPublic])
def get_character_games(character_id: int, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character.games
@app.get("/games/{game_id}/sessions", response_model=List[GamesPublic])
def get_game_sessions(game_id: int, session: Session = Depends(get_session)):
    game = session.get(Games, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game.sessions
