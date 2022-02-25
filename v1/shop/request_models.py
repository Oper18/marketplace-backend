# coding: utf-8

from typing import Optional, List, Dict

from pydantic import BaseModel, Field


class SerialNumberRequest(BaseModel):
    serial_number: str = Field(description="Product serial number")
