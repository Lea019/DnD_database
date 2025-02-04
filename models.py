from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel



class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    c_class: str
    attribute: str #list
    image: str #link or fichier??
    max_hp: int
    current_hp: int
    level: int
    initiative: int
    defence: int
    inventory: str
        
    current_state: Optional[str] = Field(default=None, index=True)
    damage_per_turn: Optional[int] = Field(default=None, index=True)
    spell_in_action: Optional[str] = Field(default=None, index=True)


    notes: Optional[str] = Field(default=None, index=True)


    game_id: Optional[int] = Field(default=None, foreign_key="game.id")
    game: Optional["game"] = Relationship(back_populates="characters")


class Actions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    a_type: str
    name: str
    a_range: int
    time: int
    damage: int
    attribute: str 
    description

class Weapons(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    w_type: str
    name: str
    w_range: int
    damage: int
    attribute: str 

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    date: str
    time: int
    chartes_pics: str #image


    characters: List["Character"] = Relationship(back_populates="game")