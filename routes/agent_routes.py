from logs.log import logger
from models.models import Agent, UpdateAgent
from fastapi import APIRouter, HTTPException
from database.agent_db import AgentDB
from database.db_connection import DB_connection
agent_db = AgentDB("db")


router = APIRouter(prefix="/agents", tags=["agents"])

@router.post("", status_code=201)
def creat_agent(body: Agent):
    logger.info("POST/ creat_agent called")
    try:
        data = body.model_dump()
        data["agent_rank"] = data["agent_rank"].value
        print(data)
        return  agent_db.create_agent(data)
        logger.info()
    except Exception as e:
        logger.error(500, f"{e}")
        raise HTTPException(500, f"{e}")
@router.get("")
def get_agents():
    logger.info("GET / get_agents called" )
    try:
        return agent_db.get_all_agents()
        logger.info()
    except Exception as e:
        logger.error(500, f"{e}")
        raise HTTPException(500, f"{e}")

@router.get("/{id}")
def get_agent(id: int):
    logger.info("GET / get_agent called")
        
    if  not agent_db.is_id(id):
            logger.error("id not found")
            raise HTTPException(404, "id not found")
    try:

        return agent_db.get_agent_by_id(id)
        logger.info()
    except Exception as e:
        logger.error(500, f"{e}")
        raise HTTPException(500, f"{e}")



@router.put("/{id}/deactivate")
def deactivate(id: int):
    logger.info("PUT/ deactivate called")
    if  not agent_db.is_id(id):
            raise HTTPException(404, "id not found")
    try:
        return agent_db.deactivate_agent(id)
        logger.info()
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")
    
@router.put("/{id}")
def update_agent(id: int, body: UpdateAgent):
    logger.info("PUT/ update_agent called")
    if  not agent_db.is_id(id):
            raise HTTPException(404, "id not found")
    try:
        data = body.model_dump()
        data["agent_rank"] = data["agent_rank"].value
        return  agent_db.update_agent(id, data)
        logger.info()
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")

@router.get("/{id}/performance")
def agent_performance(id: int):
    logger.info("GET/ agent_performance called")
    if  not agent_db.is_id(id):
            raise HTTPException(404, "id not found")
    try:
        return agent_db.get_agent_performance(id)
        logger.info()
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")






