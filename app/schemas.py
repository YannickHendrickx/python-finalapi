# Imports
from pydantic import BaseModel

# Project schemas
class ProjectBase(BaseModel):
    projectName: str

class ProjectAdd(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Student schemas
class studentBase(BaseModel):
    name: str

class studentAdd(studentBase):
    pass

class student(studentBase):
    id: int
    projects: list[Project] = []

    class Config:
        orm_mode = True

# Coach schemas
class coachBase(BaseModel):
    name: str

class coachAdd(coachBase):
    password: str

class coach(coachBase):
    id: int
    is_active: bool
    hashed_password: str

    class Config:
        orm_mode = True