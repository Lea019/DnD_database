from typing import TYPE_CHECKING, Optional, Dict, List
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from datetime import date

class GameCharacterLink(SQLModel, table=True):
    game_id: Optional[int] = Field(default=None, foreign_key="games.id", primary_key=True)
    character_id: Optional[int] = Field(default=None, foreign_key="characters.id", primary_key=True)

class PlayerCharacterLink(SQLModel, table=True):
    player_id: Optional[int] = Field(default=None, foreign_key="players.id", primary_key=True)
    character_id: Optional[int] = Field(default=None, foreign_key="characters.id", primary_key=True)

class GamePlayersLink(SQLModel, table=True):
    player_id: Optional[int] = Field(default=None, foreign_key="players.id", primary_key=True)
    game_id: Optional[int] = Field(default=None, foreign_key="games.id", primary_key=True)
   
class CharacterActionsLink(SQLModel, table=True):
    character_id: Optional[int] = Field(default=None, foreign_key="characters.id", primary_key=True)
    action_id: Optional[int] = Field(default=None, foreign_key="actions.id", primary_key=True)

class CharacterWeaponsLink(SQLModel, table=True):
    character_id: Optional[int] = Field(default=None, foreign_key="characters.id", primary_key=True)
    weapon_id: Optional[int] = Field(default=None, foreign_key="weapons.id", primary_key=True)
   
class GameSessionsLink(SQLModel, table=True):
    game_id: Optional[int] = Field(default=None, foreign_key="games.id", primary_key=True)
    session_id: Optional[int] = Field(default=None, foreign_key="sessions.id", primary_key=True)
   
class SessionPlayerLink(SQLModel, table=True):
    session_id: Optional[int] = Field(default=None, foreign_key="sessions.id", primary_key=True)
    player_id: Optional[int] = Field(default=None, foreign_key="players.id", primary_key=True)
    
class CharactersBase(SQLModel):
    name: str = Field(index=True)
    c_class: str
    #attributes:
    strength: Optional[int] = Field(default=0, gt=-5, le=30)
    dexterity:  Optional[int] = Field(default=0, gt=-5, le=30)
    constitution:  Optional[int] = Field(default=0, gt=-5, le=30)
    intelligence: Optional[int] = Field(default=0, gt=-5, le=30)
    wisdom: Optional[int] = Field(default=0, gt=-5, le=30)
    charisma: Optional[int] = Field(default=0, gt=-5, le=30)

    image: str #link or fichier??
    max_hp: int
    current_hp: int
    level: Optional[int] = Field(default=0, gt=-1)
    initiative: Optional[int] = Field(default=0)
    defence: Optional[int] = Field(default=0)
    inventory: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))

    current_state: Optional[str] = Field(default=None)
    damage_per_turn: Optional[int] = Field(default=None)
    spell_in_action: Optional[str] = Field(default=None)

    notes: Optional[str] = Field(default=None)

    
class Characters(CharactersBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    games: List["Games"] = Relationship(back_populates="characters", link_model=GameCharacterLink)
    players: List["Players"] = Relationship(back_populates="characters", link_model=PlayerCharacterLink)
    actions: List["Actions"] = Relationship(back_populates="characters", link_model=CharacterActionsLink)
    weapons: List["Weapons"] = Relationship(back_populates="characters", link_model=CharacterWeaponsLink)

class CharactersCreate(CharactersBase):
    pass
class CharactersPublic(CharactersBase):
    id: int
    players: List["PlayersPublic"] = []
    games: List["GamesPublic"] = []
    actions: List["ActionsPublic"] = []
    weapons: List["WeaponsPublic"] = []

class CharactersUpdate(SQLModel):
    name: str | None = None
    c_class: str | None = None
    #attributes:
    strength: int | None = None
    dexterity:  int | None = None
    constitution:  int | None = None
    intelligence: int | None = None
    wisdom: int | None = None
    charisma: int | None = None

    image: str | None = None
    max_hp: int | None = None
    current_hp: int | None = None
    level: int | None = None
    initiative: int | None = None
    defence: int | None = None
    inventory: List[str] | None = None
        
    current_state: str | None = None
    damage_per_turn: int | None = None
    spell_in_action: str | None = None

    notes: str | None = None

    

class ActionsBase(SQLModel):
    name: str = Field(index=True)
    a_type: str
    a_range: str
    time: str
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
class Actions(ActionsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

    characters: List["Characters"] = Relationship(back_populates="actions", link_model=CharacterActionsLink)
class ActionsCreate(ActionsBase):
    pass
class ActionsPublic(ActionsBase):
    id: int
class ActionsUpdate(SQLModel):
    name: str | None = None
    a_type: str | None = None
    a_range: str | None = None
    time: str | None = None
    damage: int | None = None
    attribute: str | None = None
    description: str | None = None

class WeaponsBase(SQLModel):
    w_name: str = Field(index=True)
    w_type: str
    w_range: int
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
class Weapons(WeaponsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  

    characters: List["Characters"] = Relationship(back_populates="weapons", link_model=CharacterWeaponsLink) 
class WeaponsCreate(WeaponsBase):
    pass
class WeaponsPublic(WeaponsBase):
    id: int
class WeaponsUpdate(SQLModel):
    w_name: str | None = None
    w_type: str | None = None
    w_range: int | None = None
    damage: int | None = None
    attribute: str | None = None
    description: str | None = None

class GamesBase(SQLModel):
    name: str = Field(index=True)
    chartes_pics: str #image

    
class Games(GamesBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    characters: List["Characters"] = Relationship(back_populates="games", link_model=GameCharacterLink)
    players: List["Players"] = Relationship(back_populates="games", link_model=GamePlayersLink)
    sessions: List["Sessions"] = Relationship(back_populates="games", link_model=GameSessionsLink)


class GamesCreate(GamesBase):
    pass
class GamesPublic(GamesBase):
    id: int
    characters: List["CharactersPublic"] = []
    players: List["PlayersPublic"] = []
    sessions: List["SessionsPublic"] = []
class GamesUpdate(SQLModel):
    name: str | None = None
    chartes_pics: str | None = None


class SessionsBase(SQLModel):
    name: str = Field(index=True)
    session_date: date
    notes: Optional[str] = Field(default=None)

class Sessions(SessionsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  

    players: List["Players"] = Relationship(back_populates="sessions", link_model=SessionPlayerLink)
    games: List["Games"] = Relationship(back_populates="sessions", link_model=GameSessionsLink)
class SessionsCreate(SessionsBase):
    pass
class SessionsPublic(SessionsBase):
    id: int
    games: List["GamesPublic"] = []
    players: List["PlayersPublic"] = []
class SessionsUpdate(SQLModel):
    name: str | None = None
    session_date: date | None = None
    notes: str | None = None
    



class PlayersBase(SQLModel):
    name: str = Field(index=True)

class Players(PlayersBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

    characters: List["Characters"] = Relationship(back_populates="players", link_model=PlayerCharacterLink)
    games: List["Games"] = Relationship(back_populates="players", link_model=GamePlayersLink)


class PlayersCreate(PlayersBase):
    pass
class PlayersPublic(PlayersBase):
    id: int
    characters: List["CharactersPublic"] = []
    games: List["GamesPublic"] = []
class PlayersUpdate(SQLModel):
    name: str | None = None



