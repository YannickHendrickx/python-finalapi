# Imports
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Coach(Base):
    __tablename__ = "Coaches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String, index=True)
    is_active = Column(Boolean, default=True)

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "Projects"

    id = Column(Integer, primary_key=True, index=True)
    projectName = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("Students.id"))

    owner = relationship("Student", back_populates="projects")