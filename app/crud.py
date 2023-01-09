# Imports
from sqlalchemy.orm import Session
import auth, models, schemas

# Get coach
def get_coach(db: Session, coach_id: int):
    return db.query(models.Coach).filter(models.Coach.id == coach_id).first()

# Get Coach by name
def get_coach_by_name(db: Session, name: str):
    return db.query(models.Coach).filter(models.Coach.name == name).first()

# Get all Coaches
def get_coaches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coach).offset(skip).limit(limit).all()

# get coach by provided id
def get_coach(db: Session, coach_id: int):
    coach_by_id = db.query(models.Coach).filter(models.Coach.id == coach_id).first()
    return coach_by_id

# Add new coach
def create_coach(db: Session, coach: schemas.coachAdd):
    hashed_password = auth.get_password_hash(coach.password)
    db_coach = models.Coach(name=coach.name, hashed_password=hashed_password)
    db.add(db_coach)
    db.commit()
    db.refresh(db_coach)
    return db_coach

# Delete specific coach
def delete_coach(db: Session, coach_id: int):
    db_coach = db.query(models.Coach).filter(models.Coach.id == coach_id).first()
    db.delete(db_coach)
    db.commit()
    return db_coach

# Update specific coach
def update_coach(db: Session, coach_id: int, coach: schemas.coachAdd):
    hashed_password = auth.get_password_hash(coach.password)
    db_coach = db.query(models.Coach).filter(models.Coach.id == coach_id).first()
    db_coach.name = coach.name
    db_coach.password = hashed_password
    db.commit()
    db.refresh(db_coach)
    return db_coach

# get student by provided id
def get_student(db: Session, student_id: int):
    student_by_id = db.query(models.Student).filter(models.Student.id == student_id).first()
    return student_by_id

# get all Students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    all_students = db.query(models.Student).offset(skip).limit(limit).all()
    return all_students

# Add new student
def add_student(db: Session, student: schemas.studentAdd):
    # hashed_password = auth.get_password_hash(student.password)
    # db_student = models.Student(name=student.name, hashed_password= hashed_password)
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# get all projects
def get_project(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

# Add new project to student
def create_student_project(db: Session, project: schemas.studentAdd, student_id: int):
    db_project = models.Project(**project.dict(), owner_id=student_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project