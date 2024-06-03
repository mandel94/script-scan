from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .session import engine


Base = declarative_base()


class Script(Base):
    __tablename__ = 'scripts'

class Script(Base):
    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    raw_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    scenes = relationship('Scene', back_populates='script', cascade='all, delete-orphan')
    characters = relationship('Character', back_populates='script', cascade='all, delete-orphan')
    dialogues = relationship('Dialogue', back_populates='script', cascade='all, delete-orphan')
    transitions = relationship('Transition', back_populates='script', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Script {self.title}>'

class Scene(Base):
    __tablename__ = 'scenes'

    id = Column(Integer, primary_key=True)
    script_id = Column(Integer, ForeignKey('scripts.id'))
    content = Column(Text, nullable=False)
    script = relationship('Script', back_populates='scenes')

class Dialogue(Base):
    __tablename__ = 'dialogues'

    id = Column(Integer, primary_key=True)
    script_id = Column(Integer, ForeignKey('scripts.id'))
    character = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    script = relationship('Script', back_populates='dialogues')

class Transition(Base):
    __tablename__ = 'transitions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    script_id = Column(Integer, ForeignKey('scripts.id'))
    name = Column(String, nullable=False)
    script = relationship('Script', back_populates='characters')


Base.metadata.create_all(engine) 