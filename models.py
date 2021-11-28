from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(String)
    position = Column(String)
    club_id = Column(Integer, ForeignKey("club.id"))

    club = relationship("Club")


class Club(Base):
    __tablename__ = "club"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)

