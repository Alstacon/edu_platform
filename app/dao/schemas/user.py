import uuid

from fastapi import HTTPException
from pydantic import EmailStr, BaseModel, validator

from app.dao.models.user import Base
from app.tools import NAMES_PATTERN


class ShowUser(Base):
    """Response with user's data"""
    id: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

    @validator('first_name')
    def validate_name(cls, value):
        if not NAMES_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='First name and last name should consists only letters')
        else:
            return value

    @validator('last_name')
    def validate_last_name(cls, value):
        if not NAMES_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='First name and last name should consists only letters')
        else:
            return value
