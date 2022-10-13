from pydantic import BaseModel

class Message(BaseModel):
    contacts:list
    context:str
    