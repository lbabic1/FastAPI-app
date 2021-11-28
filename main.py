import uvicorn
from fastapi import FastAPI, applications
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
import os

from models import Club
from models import Player
from schema import Player as SchemaPlayer
from schema import Club as SchemaClub

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/add-player/", response_model=SchemaPlayer)
def add_player(player: SchemaPlayer):
    db_player = Player(name=player.name, date_of_birth=player.date_of_birth, position=player.position, club_id=player.club_id)
    db.session.add(db_player)
    db.session.commit()
    return db_player

@app.post("/add-club/", response_model=SchemaClub)
def add_club(club: SchemaClub):
    db_club = Club(name=club.name, country=club.country)
    db.session.add(db_club)
    db.session.commit()
    return db_club

@app.get("/player/")
def get_players():
    players = db.session.query(Player).all()
    return players


@app.get("/player/{id}")
def get_player(id:int):
    player = db.session.query(Player).filter(Player.id==id).first()
    return player

@app.put("/player/{id}")
def update_player(id:int, position:str, club_id:int):
    db_player = get_player(id=id)
    db_player.position = position
    db_player.club_id = club_id

    db.session.commit()
    db.session.refresh(db_player) 
    return db_player

@app.delete("/{id}")
def delete_player(id:int):
    db_player = get_player(id=id)
    db.session.delete(db_player)
    db.session.commit()