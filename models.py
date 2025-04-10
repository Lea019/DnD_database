from typing import TYPE_CHECKING, Optional, Dict, List
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime



class CharactersBase(SQLModel):
    name: str = Field(index=True)
    c_class: str
    #attributes:
    strength: Optional[int] = Field(default=0, gt=-5, le=30)
    dexterity:  Optional[int] = Field(default=0, gt=-5, le=30)
    consititution:  Optional[int] = Field(default=0, gt=-5, le=30)
    intelligence: Optional[int] = Field(default=0, gt=-5, le=30)
    wisdom: Optional[int] = Field(default=0, gt=-5, le=30)
    charisma: Optional[int] = Field(default=0, gt=-5, le=30)

    image: str #link or fichier??
    max_hp: int
    current_hp: int
    level: Optional[int] = Field(default=0, gt=0)
    initiative: Optional[int] = Field(default=0)
    defence: Optional[int] = Field(default=0)
    inventory: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    
        
    current_state: Optional[str] = Field(default=None)
    damage_per_turn: Optional[int] = Field(default=None)
    spell_in_action: Optional[str] = Field(default=None)


    notes: Optional[str] = Field(default=None)

class Characters(CharactersBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
class CharactersCreate(CharactersBase):
    pass
class CharactersPublic(CharactersBase):
    id: int
   
class ActionsBase(SQLModel):
    a_type: str
    name: str = Field(index=True)
    a_range: str
    time: str
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

class Actions(ActionsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)   
class ActionsCreate(ActionsBase):
    pass
class ActionsPublic(ActionsBase):
    id: int
    

class WeaponsBase(SQLModel):
    w_type: str
    w_name: str = Field(index=True)
    w_range: int
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

class Weapons(WeaponsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)   
class WeaponsCreate(WeaponsBase):
    pass
class WeaponsPublic(WeaponsBase):
    id: int
    
class GamesBase(SQLModel):
    name: str = Field(index=True)
    session_datetime: datetime
    chartes_pics: str #image

class Games(GamesBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
class GamesCreate(GamesBase):
    pass
class GamesPublic(GamesBase):
    id: int

class PlayersBase(SQLModel):
    name: str = Field(index=True)

class Players(PlayersBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
class PlayersCreate(PlayersBase):
    pass
class PlayersPublic(PlayersBase):
    id: int


    
    