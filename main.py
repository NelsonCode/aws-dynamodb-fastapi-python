from fastapi import FastAPI
from database.db import create_tables
from routes.user import routes_user


app = FastAPI()


app.include_router(routes_user, prefix="/user")

create_tables()