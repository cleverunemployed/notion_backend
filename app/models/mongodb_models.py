from pydantic import BaseModel

class MongoItem(BaseModel):
    id: str
    name: str
    description: str
