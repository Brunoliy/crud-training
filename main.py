from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models import User
from database import engine, Base, get_db
from repositories import UserRepository
from schemas import UserRequest, UserResponse

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create an instance of the FastAPI class
app = FastAPI()

# Create a route that creates a new user
@app.post("/api/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    user = UserRepository.save(db, User(**request.dict()))
    return UserResponse.from_orm(user)

# Create a route that returns all users
@app.get("/api/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = UserRepository.find_all(db)
    return [UserResponse.from_orm(user) for user in users]
    

# Create a route that returns a user by id
@app.get("/api/users/{id}", response_model=UserResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.find_by_id(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse.from_orm(user)

# Create a route that deletes a user by id
@app.delete("/api/users/{id}")
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    UserRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Create a route that updates a user by id
@app.put("/api/users/{id}", response_model=UserResponse)
def update_user(id: int, request: UserRequest, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user = UserRepository.save(db, User(id=id, **request.dict()))
    return UserResponse.from_orm(user)
