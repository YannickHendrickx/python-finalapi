#!/usr/bin/python3

# Imports
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud, models, schemas, auth
import os


# ----------------
#  Final API assignment
# ----------------
# Yannick Hendrickx
# r0615765

# make database dir if it doesn't exist
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# create tables in database 'sqlitedata.db' (check datapase.py database-URL)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# make database session/connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# allowed origins for CORS
origins = ["*"]

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

# Add authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    coach = auth.authenticate_user(db, form_data.username, form_data.password)
    if not coach:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(coach)
    access_token = auth.create_access_token(
        data={"sub": coach.name}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

# Get information about current logged in user
@app.get("/coaches/me", response_model=schemas.coach)
async def read_coaches_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user

# Add new coach
@app.post("/coaches/", response_model=schemas.coach)
async def create_coach(coach: schemas.coachAdd, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_coach = crud.get_coach_by_name(db, name=coach.name)
    if db_coach:
        raise HTTPException(status_code=400, detail="Coach already registered")
    return crud.create_coach(db=db, coach=coach)

# Get all coaches
@app.get("/coaches/", response_model=list[schemas.coach])
async def read_coaches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    coaches = crud.get_coaches(db, skip=skip, limit=limit)
    return coaches

# Get specific coach
@app.get("/coaches/{coach_id}", response_model=schemas.coach)
async def read_coach(coach_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_coach = crud.get_coach(db, coach_id=coach_id)
    if db_coach is None:
        raise HTTPException(status_code=404, detail="Coach not found!")
    return db_coach

# Delete specific coach
@app.delete("/coaches/{coach_id}", response_model=schemas.coach)
async def delete_coach(coach_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_coach = crud.delete_coach(db, coach_id=coach_id)
    if db_coach is None:
        raise HTTPException(status_code=404, detail="Coach not found!")
    return db_coach

# Update specific coach
@app.put("/coaches/{coach_id}")
async def update_coach(coach_id: int, coach: schemas.coachAdd, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_coach = crud.update_coach(db, coach_id=coach_id, coach=coach)
    return db_coach

# get all students
@app.get("/students/all", response_model=list[schemas.student])
async def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

# Get specific student
@app.get("/students/{student_id}", response_model=schemas.student)
async def read_student(student_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return db_student

# Add new student
@app.post("/students/", response_model=schemas.student)
async def add_student(student: schemas.studentAdd, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    add_student = crud.add_student(db=db, student=student)
    return add_student

# Add a new project to specific student
@app.post("/students/{student_id}/projects/", response_model=schemas.Project)
async def create_student_project(student_id: int, project: schemas.ProjectAdd, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.create_student_project(db=db, project=project, student_id=student_id)

# Get all projects
@app.get("/projects/", response_model=list[schemas.Project])
async def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_project(db, skip=skip, limit=limit)
    return projects