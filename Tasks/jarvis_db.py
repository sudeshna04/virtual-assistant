from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    tid = Column(Integer, primary_key=True)
    name=Column(String)
    status = Column(String)
    priority = Column(String)
    notes = relationship("Note", back_populates="task")

# NOTE Entity
class Note(Base):
    __tablename__ = 'notes'
    nid = Column(Integer, primary_key=True)
    data = Column(Text)
    priority = Column(String)
    tid = Column(Integer, ForeignKey('tasks.tid'))
    parent_id = Column(Integer, ForeignKey('notes.nid'), nullable=True)

    task = relationship("Task", back_populates="notes")
    parent = relationship("Note", remote_side=[nid], backref="sub_notes")

# DB Setup
engine = create_engine("sqlite:///jarvis.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
