# coding: utf-8

import os
import re

from functools import wraps

from typing import Optional, Union

from fastapi import APIRouter, status, Response, Request, Query

from .response_models import (
    ProductListResponse,
    NewsListResponse,
    ProductResponse,
    CategoryListResponse,
    CategoryResponse,
)
from .request_models import SerialNumberRequest

from response_models import Error40xResponse

from models.models import Product, New, ProductSerialNumber, Category

from settings import IMG_PATH


router = APIRouter(
    prefix="/v1/shop",
    tags=["shop"]
)


def replace_lang(func):
    @wraps(func)
    async def wrapper(**kwargs):
        if kwargs.get("lang"):
            kwargs["lang"] = ("_" + re.sub("_", "", kwargs.get("lang"))).lower()
        else:
            kwargs["lang"] = "_ru"
        return await func(**kwargs)
    return wrapper


async def get_records(
    model,
    pk: Optional[int] = None,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    additional_filter: Optional[dict] = {},
):
    amount = await model.all().count()
    if pk:
        model = model.filter(id=pk)
    else:
        if additional_filter:
            model = model.filter(**additional_filter)
        else:
            model = model.all()
        model = model.\
            limit(limit).\
            offset(offset)

    return amount, model


@router.get(
    "/categories",
    responses={
        200: {
            "model": CategoryListResponse,
            "description": "products list with full count",
        },
        400: {
            "model": Error40xResponse,
            "description": "something wrong",
        },
    },
    summary="Product list",
)
@replace_lang
async def get_products(
    request: Request,
    response: Response,
    category_id: Optional[int] = Query(None, description="category pk"),
    limit: Optional[int] = Query(10, description="amount of returned products"),
    offset: Optional[int] = Query(0, description="amount of scrolled products"),
    lang: Optional[str] = Query("ru", description="iso 2 symbols format of language"),
) -> ProductListResponse:
    categories_count, categories = await get_records(
        model=Category,
        pk=category_id,
        limit=limit,
        offset=offset,
    )
    categories = await categories

    res = {
        "count": categories_count,
        "categories": [],
    }
    for c in categories:
        cd = await c.as_dict()
        cd["manufacturers"] = {}
        for p in await c.products.all():
            if p.manufacturer:
                pm = await p.manufacturer.first()
                cd["manufacturers"][pm.id] = await pm.as_dict()
        cd["manufacturers"] = list(cd["manufacturers"].values())
        res["categories"].append(cd)

    return CategoryListResponse.parse_obj(res)


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
@replace_lang
async def get_products(
    request: Request,
    response: Response,
    product_id: Optional[int] = Query(None, description="product pk"),
    category_id: Optional[int] = Query(None, description="category pk"),
    manufacturer_id: Optional[int] = Query(None, description="manufacturer pk"),
    limit: Optional[int] = Query(10, description="amount of returned products"),
    offset: Optional[int] = Query(0, description="amount of scrolled products"),
    lang: Optional[str] = Query("ru", description="iso 2 symbols format of language"),
) -> ProductListResponse:
    additional_filter = {}
    if category_id:
        additional_filter["category__pk"] = category_id
    if manufacturer_id:
        additional_filter["manufacturer__pk"] = manufacturer_id
    products_count, products = await get_records(
        model=Product,
        pk=product_id,
        limit=limit,
        offset=offset,
        additional_filter=additional_filter,
    )
    products = await products

    res = {
        "count": products_count,
        "products": [],
    }
    for p in products:
        pd = await p.as_dict(lang=lang)
        pd["img"] = os.path.join(IMG_PATH, os.path.basename(pd["img"])) if pd.get("img") else None
        if p.category:
            product_category = await p.category.first()
            pd["category"] = await product_category.as_dict()
        else:
            pd["category"] = None
        if p.manufacturer:
            product_manufacturer = await p.manufacturer.first()
            pd["manufacturer"] = await product_manufacturer.as_dict()
        else:
            pd["manufacturer"] = None
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
@replace_lang
async def get_news(
    request: Request,
    response: Response,
    new_id: Optional[int] = Query(None, description="new pk"),
    limit: Optional[int] = Query(10, description="amount of returned news"),
    offset: Optional[int] = Query(0, description="amount of scrolled news"),
    lang: Optional[str] = Query("ru", description="iso 2 symbols format of language"),
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
        nd = await n.as_dict(lang=lang)
        nd["banner"] = os.path.join(IMG_PATH, os.path.basename(nd["banner"])) \
            if nd.get("banner") else None
        if n.product:
            nd["product"] = await n.product.as_dict(lang=lang)
            nd["product"]["img"] = os.path.join(IMG_PATH, os.path.basename(nd["product"]["img"])) \
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
@replace_lang
async def check_article_number(
    request: Request,
    response: Response,
    num: SerialNumberRequest,
    lang: Optional[str] = Query("ru", description="iso 2 symbols format of language"),
) -> Union[ProductResponse, Error40xResponse]:
    ser_num = await ProductSerialNumber.\
        filter(serial_number=num.serial_number).\
        first()
    if ser_num:
        res = await ser_num.product
        if res:
            res = await res.as_dict(lang=lang)
            res["img"] = os.path.join(IMG_PATH, os.path.basename(res["img"])) if res.get("img") else None
            return ProductResponse.parse_obj(res)
        else:
            return Error40xResponse(reason="serial number exist")
    return Error40xResponse.parse_obj(
        {"reason": "wrong serial number"}
    )
