from pydantic import BaseModel, Field
from typing import Literal


class Type(BaseModel):
    type: Literal["open", "close"]
    value: int = Field(lt=86400, gt=-1)


class OpeningHours(BaseModel):
    monday: list[Type] | None
    tuesday: list[Type] | None
    wednesday: list[Type] | None
    thursday: list[Type] | None
    friday: list[Type] | None
    saturday: list[Type] | None
    sunday: list[Type] | None
