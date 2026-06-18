from logs.log import logger
from models.models import Mission, UpdateAgent
from fastapi import APIRouter, HTTPException
from services.db_servis_servis import *
from database.mission_db import MissionDB
from database.agent_db import AgentDB
mission_db = MissionDB("db")
agent_db = AgentDB("db")

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/summary")
def summary():
    logger.info("POT/ summary called")
    try:
        return {
"active_agents_count": agent_db.count_active_agent(),
"total_missions": mission_db.count_all_missions(),
"open_missions": mission_db.count_open_missions,
"completed_missions": mission_db.count_by_status("COMPLETED"),
"failed_missions": mission_db.count_by_status("FAILED"),
"critical_missions": mission_db.count_critical_missions()
}
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")
    
@router.get("/missions-by-status")
def by_status():
    logger.info("POT/ start_mission called")
    try:
        return {
"open": mission_db.count_open_missions(),
"in_progress": mission_db.count_by_status("IN_PROGRESS"),
"completed": mission_db.count_by_status("COMPLETED"),
"failed": mission_db.count_by_status("FAILED"),
"cancelled": mission_db.count_by_status("CANCELLED")
}

    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")
    
@router.get("/top-agent")
def top_agent():
    logger.info("POT/ top_agent called")
    try:
        return {
"active_agents_count": agent_db.count_active_agent(),
"total_missions": mission_db.count_all_missions(),
"open_missions": mission_db.count_open_missions,
"completed_missions": mission_db.count_by_status("COMPLETED"),
"failed_missions": mission_db.count_by_status("FAILED"),
"critical_missions": mission_db.count_critical_missions()
}
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(500, f"{e}")