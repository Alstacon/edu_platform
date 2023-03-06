from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        '''Pydentic will convert to JSON even non-dict obj'''
        orm_mode = True
