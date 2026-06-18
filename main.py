from  fastapi import FastAPI
from routes import agent_routes, mission_routes, report_routes
from uvicorn import run
from database.db_connection import DB_connection

app = FastAPI()

app.include_router(agent_routes.router)
app.include_router(mission_routes.router)
app.include_router(report_routes.router)

if __name__ == "__main__":
    connection = DB_connection()
    connection.create_database()
    connection.create_tables()
    run("main:app", reload=True)