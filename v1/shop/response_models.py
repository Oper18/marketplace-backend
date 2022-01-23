# coding: utf-8

from typing import Optional, List

from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    id: int = Field(description="product pk")
    name: str = Field(description="product name")
    full_name: str = Field(description="product full name")
    description: str = Field(description="product description")
    sketches: str = Field(description="product short description")
    img: str = Field(description="product img filepath")
    created_at: str = Field(description="date of record creation")
    updated_at: str = Field(description="date of record last update")


class ProductListResponse(BaseModel):
    count: int = Field(description="full amount of products records")
    products: List[ProductResponse] = Field(description="products list")


class NewResponse(BaseModel):
    id: int = Field(description="new pk")
    head: str = Field(description="new title")
    text: str = Field(description="new text")
    product: Optional[ProductResponse] = Field(
        description="new product response if exist"
    )
    banner: Optional[str] = Field(description="new banner path")
    created_at: str = Field(description="date of record creation")
    updated_at: str = Field(description="date of record last update")


class NewsListResponse(BaseModel):
    count: int = Field(description="full amount of news")
    news: List[NewResponse] = Field(description="news list")
