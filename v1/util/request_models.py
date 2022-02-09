# coding: utf-8

from typing import Optional

from pydantic import BaseModel, Field


class BidRequest(BaseModel):
    name: str = Field(description="name of bid author")
    email: str = Field(description="contacts for reverse contact")
    message: Optional[str] = Field(description="additional info")
