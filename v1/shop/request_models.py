# coding: utf-8

from typing import Optional, List, Dict

from pydantic import BaseModel, Field


class SerialNumberRequest(BaseModel):
    serial_number: int = Field(description="Product serial number")
