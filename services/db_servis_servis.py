from logs.log import logger
from database.agent_db import AgentDB
from database.mission_db import MissionDB
from database.db_connection import DB_connection
agent_db = AgentDB("db")
mission_db = MissionDB("db")


def create_risk_level(importance,  difficulty):
    risk_level = difficulty * 2 + importance
    if risk_level < 10:
        return "LOW"
    elif risk_level <= 17:
        return "MEDIUM"
    elif risk_level < 24:
        return "HIGH"
    else: 
        return "CRITICAL"
    
def criti_for_commader(a_id, m_id):
    risk_level = mission_db.get_mission_by_id(m_id)[0]["risk_level"]
    if risk_level != "CRITICAL":
        return True
    if agent_db.is_commender(a_id):
        return True
    return False
def is_new(id):
    status = mission_db.get_mission_by_id(id)[0]["status"]
    if status == "NEW":
        return True
    return False


def create_mission_validition(agent: dict):
    #בדיקה שזה  1-10
    if not (0 < agent["importance"] <= 10) or not (0 < agent["difficulty"] <= 10):
        raise ValueError("most be 1 - 10")
    
    agent["risk_level"] = create_risk_level(agent["importance"], agent["difficulty"])
    return mission_db.create_mission(agent)


def assign_validtion(m_id: int, a_id: int):
    if not agent_db.is_agent_active(a_id):
        raise ValueError("agent is not active")
    if not agent_db.is_id(a_id) or not mission_db.is_id(m_id):
        raise TypeError("id not found")
    if len(mission_db.get_open_missions_by_agent(a_id)) >= 3:
        raise ValueError("agent has 3 missions open")
    if not criti_for_commader(a_id, m_id):
        raise ValueError("Critical mission can assign only to a commender")
    if not is_new(m_id):
        raise ValueError("mission status is not NEW")
    logger.info("mission assigned seccfuly")
    update_status_validtion(m_id, "ASSIGNED" )
    return mission_db.assign_mission(m_id, a_id)


def update_status_validtion(id: int, new_status: str):
    status_format = ("ASSIGNED", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED")
    now_status = mission_db.get_mission_by_id(id)[0]["status"]
    if new_status not in status_format:
        raise ValueError("status not in format")
    if new_status == "ASSIGNED" and now_status != "NEW":
        raise ValueError("mission is not ASSIGNED")
    if new_status == "IN_PROGRESS" and now_status != "ASSIGNED":
        raise ValueError("mission is not ASSIGNED")
    if (new_status == "COMPLETED" or new_status == "FAILED") and now_status != "IN_PROGRESS":
        raise ValueError("mission is not IN_PROGRESS to complet it")
    if new_status == "CANCELLED" and now_status != "NEW" and now_status != "ASSIGNED":
        raise ValueError("mission can't cancelled")
    return mission_db.update_mission_status(id, new_status)
