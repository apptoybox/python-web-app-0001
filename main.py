import asyncpg
from fastapi import FastAPI

app = FastAPI()

# Database connection settings
DATABASE_URL = "postgresql://myuser:mypassword@database/mydb"


@app.on_event("startup")
async def startup():
    app.db_pool = await asyncpg.create_pool(DATABASE_URL)


@app.on_event("shutdown")
async def shutdown():
    await app.db_pool.close()


@app.get("/")
async def main():
    return {"message": "Hello, World!"}


@app.get("/users")
async def get_users():
    query = "SELECT * FROM users"
    async with app.db_pool.acquire() as connection:
        results = await connection.fetch(query)

    users = [dict(result) for result in results]
    return {"users": users}


@app.get("/user/{userid}")
async def get_user(userid: int):
    query = "SELECT * FROM users WHERE id = $1"
    async with app.db_pool.acquire() as connection:
        result = await connection.fetchrow(query, userid)

    if result:
        return dict(result)
    return {"message": "User not found"}
