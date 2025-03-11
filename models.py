from typing import TYPE_CHECKING, Optional, Dict, List
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime



class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    c_class: str
    #attributes:
    strength: int = Field(gt=-5, le=30)
    dexterity: int = Field(gt=-5, le=30)
    consititution: int = Field(gt=-5, le=30)
    intelligence: int = Field(gt=-5, le=30)
    wisdom: int = Field(gt=-5, le=30)
    charisma: int = Field(gt=-5, le=30)
    
    image: str #link or fichier??
    max_hp: int
    current_hp: int
    level: int = Field(gt=0)
    initiative: int
    defence: int
    inventory: List[str] = Field(sa_column=Column(JSON))
    
        
    current_state: Optional[str] = Field(default=None)
    damage_per_turn: Optional[int] = Field(default=None)
    spell_in_action: Optional[str] = Field(default=None)


    notes: Optional[str] = Field(default=None)


    


class Actions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    a_type: str
    name: str = Field(index=True)
    a_range: str
    time: str
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

class Weapons(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    w_type: str
    w_name: str = Field(index=True)
    w_range: int
    damage: int
    attribute: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    session_datetime: datetime
    chartes_pics: str #image


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    