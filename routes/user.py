from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemes.user import User
user = APIRouter()

@user.get('/users', response_model=list[User], tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/users', response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    conn.execute(users.insert().values(new_user))
    return new_user

@user.get('/users/{id}', response_model=User, tags=["Users"])
def get_user(id:str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/users/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id:str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', response_model=User, tags=["Users"])
def update(id:str, user: User):
    result = conn.execute(users.update().values(name = user.name, email = user.email).where(users.c.id ==id))
    return conn.execute(users.select().where(users.c.id == id)).first()

     