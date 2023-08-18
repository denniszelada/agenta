from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimestampModel(BaseModel):
    created_at: datetime = Field(datetime.utcnow())
    updated_at: datetime = Field(datetime.utcnow())


class User(TimestampModel):
    id: str
    username: str
    email: str # switch to EmailStr when langchain support pydantic>=2.1
    organization_id: int
    

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    updated_at: datetime = Field(datetime.utcnow())
    
    
class Organization(TimestampModel):
    id: str
    name: str
    description: Optional[str]
    

class OrganizationUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    