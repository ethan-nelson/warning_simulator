from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Simulation(Base):
    __tablename__ = 'simulations'
    id = Column(Integer, primary_key=True)
    authorid = Column(Integer)
    name = Column(Text)
    site = Column(Text)

