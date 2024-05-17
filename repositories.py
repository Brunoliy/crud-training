from sqlalchemy.orm import Session
from models import User


# Create a class that represents the repository of the User model
class UserRepository:

    # Create a method that returns all users
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()
    
    #Save a new user or update it
    @staticmethod
    def save(db: Session, user: User) -> User:
        if user.id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()
        return user
    
    # Create a method that returns a user by id
    @staticmethod
    def find_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()
    
    #Verify if a user exists by id
    @staticmethod
    def exists_by_id(db: Session, user_id: int) -> bool:
        return db.query(User).filter(User.id == user_id).first() is not None
    
    # Create a method that deletes a user by id
    @staticmethod
    def delete_by_id(db: Session, user_id: int) -> None:
        user = db.query(User).filter(User.id == user_id).first()
        if user is not None:
            db.delete(user)
            db.commit()