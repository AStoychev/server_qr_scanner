# NOT USE

from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime, timezone

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class BaseDBModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    # id: Optional[PyObjectId] = Field(default=None, alias="_id")
    registration_date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True



# from pydantic import BaseModel, Field
# from bson import ObjectId
# from typing import Optional
# from datetime import datetime, timezone

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid ObjectId")
#         return str(v)

# class BaseDBModel(BaseModel):
#     id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
#     # id: Optional[PyObjectId] = Field(default=None, alias="_id")
#     registration_date: datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         allow_population_by_field_name = True
#         json_encoders = {ObjectId: str}
#         arbitrary_types_allowed = True