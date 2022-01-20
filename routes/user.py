from fastapi import APIRouter
from models.user import User
from database.user import create_user, get_user, get_users, delete_user, update_user


routes_user = APIRouter()

# CREATE USER


@routes_user.post("/create", response_model=User)
def create(user: User):
    return create_user(user.dict())

# GET USER BY ID


@routes_user.get("/get/{id}")
def get_by_id(id: str):
    return get_user(id)

# GET ALL USERS


@routes_user.get("/all")
def get_all():
    return get_users()

# DELETE USER


@routes_user.post("/delete")
def create(user: User):
    return delete_user(user.dict())

# UPDATE USER


@routes_user.post("/update")
def create(user: User):
    return update_user(user.dict())
