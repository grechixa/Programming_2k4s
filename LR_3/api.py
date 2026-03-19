from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.db import get_db
from models.user import UserBase
from schemas.User_schema import UserCreate, UserResponse

app = FastAPI()

# api(user input) -> pydantic(for validation) -> sqlalchemy(translate to SQL) -> database

# create new user
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):

     db_user = UserBase(
         username=user.username,
         email=user.email
     )

     db.add(db_user)
     await db.commit()
     await db.refresh(db_user)

     return db_user

# get users list
@app.get("/users/", response_model=UserResponse)
async def user_list()