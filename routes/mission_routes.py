from logs.log import logger
from models.models import Mission, UpdateAgent
from fastapi import APIRouter, HTTPException
from services.db_servis_servis import *
from database.mission_db import MissionDB
mission_db = MissionDB("db")

router = APIRouter(prefix="/missions", tags=["missions"])

@router.post("", status_code=201)
def create_mission(body : Mission):
    logger.info("POST/ create_mission called")
    try:
        data = body.model_dump()
        return create_mission_validition(data)
        logger.info()
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")
@router.get("")
def get_missions():
    logger.info("GET/ get_missions called" )
    try:
        return mission_db.get_all_missions()
        logger.info()
    except Exception as e:
        logger.error()

@router.get("/id")
def get_mission(id: int):
    logger.info("GET/ get_mission called" )
    if  not agent_db.is_id(id):
        logger.error("id not found")
        raise HTTPException(404, "id not found")
    try:
        return mission_db.get_mission_by_id(id)
        logger.info()
    except Exception as e:
        logger.error()
        raise HTTPException(500, f"{e}")

@router.put("/{id}/assign/{agent_id}")
def assing_mission(id: int, agent_id: int):
    logger.info("PUT/ assing_mission called")
    try:
        return assign_validtion(id, agent_id)
        logger.info()
    except TypeError:
        raise HTTPException(404, "id not found")
    except ValueError as e:
        raise HTTPException(400,f"{e}")
    except Exception as e:
        logger.error()
        raise HTTPException(500, f"{e}")


@router.put("/{id}/start")
def start_mission(id):
    logger.info("POT/ start_mission called")
    if  not agent_db.is_id(id):
        logger.error("id not found")
        raise HTTPException(404, "id not found")
    try:
        return update_status_validtion(id, "IN_PROGRESS")
        logger.info()
    except ValueError as e:
        logger.error(f"{e}")
        raise HTTPException(400, f"{e}")
    except Exception as e:
        logger.error()

@router.put("/{id}/complete")
def complete_mission(id):
    logger.info("POT/ complete_mission called")
    if  not agent_db.is_id(id):
        logger.error("id not found")
        raise HTTPException(404, "id not found")
    try:
        return update_status_validtion(id, "COMPLETED")
        logger.info()
    except ValueError as e:
        logger.error(f"{e}")
        raise HTTPException(400, f"{e}")
    except Exception as e:
        logger.error()

@router.put("/{id}/fail")
def fail_mission(id):
    logger.info("POT/ fail_mission called")
    if  not agent_db.is_id(id):
        logger.error("id not found")
        raise HTTPException(404, "id not found")
    try:
        return update_status_validtion(id, "FAILED")
        logger.info()
    except ValueError as e:
        logger.error(f"{e}")
        raise HTTPException(400, f"{e}")
    except Exception as e:
        logger.error()


@router.put("/{id}/cancel")
def cancel_mission(id):
    logger.info("POT/ cancel_mission called")
    if  not agent_db.is_id(id):
        logger.error("id not found")
        raise HTTPException(404, "id not found")
    try:
        return update_status_validtion(id, "CANCELD")
        logger.info()
    except ValueError as e:
        logger.error(f"{e}")
        raise HTTPException(400, f"{e}")
    except Exception as e:
        logger.error()
