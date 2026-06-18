from pydantic import BaseModel, Field
from enum import StrEnum

class RankWords(StrEnum):
    JUNIOR = "Junior"
    SENIOR = "Senior"
    COMMANDER = "Commander"



class Agent(BaseModel):
    name : str = Field(max_length=50)
    specialty : str = Field(max_length=50)
    agent_rank : RankWords

class UpdateAgent(BaseModel):
    name : str = Field(max_length=50)
    specialty : str = Field(max_length=50)
    is_active : bool
    completed_missions : int
    failed_missions : int
    agent_rank : RankWords


class Mission(BaseModel):
    title : str = Field(max_length=50)
    description : str
    location : str = Field(max_length=50)
    difficulty : int
    importance : int


class UpdateMission(BaseModel):
    title : str = Field(max_length=50)
    description : str 
    location : str = Field(max_length=50)
    difficulty : int
    importance : int
    status : str = Field(max_length=50)
    assigned_agent_id : int 