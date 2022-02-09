# coding: utf-8

from typing import List

from pydantic import BaseModel, Field


class BidRequest(BaseModel):
    contacts: str = Field(description="contacts for reverse contact")
