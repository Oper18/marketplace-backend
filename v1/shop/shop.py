# coding: utf-8

import os

from typing import Optional, Union

from fastapi import APIRouter, status, Response, Request, Query

from .response_models import (
    ProductListResponse,
    NewsListResponse,
    ProductResponse,
)
from .request_models import SerialNumberRequest

from response_models import Error40xResponse

from models.models import Product, New, ProductSerialNumber

from settings import IMG_PATH


router = APIRouter(
    prefix="/v1/shop",
    tags=["shop"]
)


async def get_records(
    model,
    pk: Optional[int] = None,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
):
    amount = await model.all().count()
    if pk:
        model = model.filter(id=pk)
    else:
        model = model.\
            all().\
            limit(limit).\
            offset(offset)

    return amount, model


@router.get(
    "/products",
    responses={
        200: {
            "model": ProductListResponse,
            "description": "products list with full count",
        },
        400: {
            "model": Error40xResponse,
            "description": "something wrong",
        },
    },
    summary="Product list",
)
async def get_products(
    request: Request,
    response: Response,
    product_id: Optional[int] = Query(None, description="product pk"),
    limit: Optional[int] = Query(10, description="amount of returned products"),
    offset: Optional[int] = Query(0, description="amount of scrolled products"),
) -> ProductListResponse:
    products_count, products = await get_records(
        model=Product,
        pk=product_id,
        limit=limit,
        offset=offset,
    )
    products = await products

    res = {
        "count": products_count,
        "products": [],
    }
    for p in products:
        pd = await p.as_dict()
        pd["img"] = os.path.join(IMG_PATH, pd["img"]) if pd.get("img") else None
        res["products"].append(pd)

    return ProductListResponse.parse_obj(res)


@router.get(
    "/news",
    responses={
        200: {
            "model": NewsListResponse,
            "description": "news list with full count",
        },
        400: {
            "model": Error40xResponse,
            "description": "something wrong",
        },
    },
    summary="News list",
)
async def get_news(
    request: Request,
    response: Response,
    new_id: Optional[int] = Query(None, description="new pk"),
    limit: Optional[int] = Query(10, description="amount of returned news"),
    offset: Optional[int] = Query(0, description="amount of scrolled news"),
) -> NewsListResponse:
    news_count, news = await get_records(
        model=New,
        pk=new_id,
        limit=limit,
        offset=offset,
    )
    news = await news.prefetch_related("product")
    res = {
        "count": news_count,
        "news": [],
    }
    for n in news:
        nd = await n.as_dict()
        nd["banner"] = os.path.join(IMG_PATH, nd["banner"]) \
            if nd.get("banner") else None
        if n.product:
            nd["product"] = await n.product.as_dict()
            nd["product"]["img"] = os.path.join(IMG_PATH, nd["product"]["img"]) \
                if nd["product"].get("img") else None
        res["news"].append(nd)

    return NewsListResponse.parse_obj(res)


@router.post(
    "/check/serial_number",
    responses={
        200: {
            "model": Union[ProductResponse, Error40xResponse],
            "description": "response with result status",
        },
        400: {
            "model": Error40xResponse,
            "description": "something wrong",
        },
    },
    summary="article number checker",
)
async def check_article_number(
    request: Request,
    response: Response,
    num: SerialNumberRequest,
) -> Union[ProductResponse, Error40xResponse]:
    ser_num = await ProductSerialNumber.\
        filter(serial_number=num.serial_number).\
        first()
    if ser_num:
        res = await ser_num.product
        res = await res.as_dict()
        res["img"] = os.path.join(IMG_PATH, res["img"]) if res.get("img") else None
        return ProductResponse.parse_obj(res)
    return Error40xResponse.parse_obj(
        {"reason": "wrong serial number"}
    )
