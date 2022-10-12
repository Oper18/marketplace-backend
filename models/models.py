# coding: utf-8

from typing import Any, Type, Optional

import datetime

from tortoise.models import Model, MODEL
from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient

from fastapi_admin.models import AbstractAdmin

from models.extensions import ExtendedModel, NewsType


class Admin(AbstractAdmin):
    pass


class Category(Model, ExtendedModel):
    _translated_fields = ("name",)

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    name_en = fields.CharField(max_length=256, null=True)
    name_de = fields.CharField(max_length=256, null=True)
    name_fr = fields.CharField(max_length=256, null=True)
    img = fields.CharField(max_length=64, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class Manufacturer(Model, ExtendedModel):
    _translated_fields = ("name",)

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    name_en = fields.CharField(max_length=256, null=True)
    name_de = fields.CharField(max_length=256, null=True)
    name_fr = fields.CharField(max_length=256, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class Product(Model, ExtendedModel):
    _translated_fields = ("name", "full_name", "description", "sketcehs")

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    name_en = fields.CharField(max_length=256, null=True)
    name_de = fields.CharField(max_length=256, null=True)
    name_fr = fields.CharField(max_length=256, null=True)
    full_name = fields.CharField(max_length=512)
    full_name_en = fields.CharField(max_length=512, null=True)
    full_name_de = fields.CharField(max_length=512, null=True)
    full_name_fr = fields.CharField(max_length=512, null=True)
    description = fields.TextField()
    description_en = fields.TextField(null=True)
    description_de = fields.TextField(null=True)
    description_fr = fields.TextField(null=True)
    sketches = fields.TextField()
    sketches_en = fields.TextField(null=True)
    sketches_de = fields.TextField(null=True)
    sketches_fr = fields.TextField(null=True)
    article_number = fields.CharField(max_length=128, null=True)
    category = fields.ForeignKeyField(
        "models.Category", related_name="products", null=True
    )
    manufacturer = fields.ForeignKeyField(
        "models.Manufacturer", related_name="products", null=True
    )
    img = fields.CharField(max_length=64, null=True)
    volume = fields.CharField(null=True, max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class ProductSerialNumber(Model, ExtendedModel):
    _exclude = ("product",)

    id = fields.IntField(pk=True)
    serial_number = fields.CharField(max_length=256, unique=True)
    product = fields.ForeignKeyField(
        "models.Product", related_name='serial_numbers', null=True
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.serial_number}"

    @classmethod
    async def create(
        cls: Type[MODEL], using_db: Optional[BaseDBAsyncClient] = None, **kwargs: Any
    ) -> MODEL:
        if not kwargs.get("product_id"):
            kwargs["product_id"] = None

        await super().create(using_db, **kwargs)


class New(Model, ExtendedModel):
    _exclude = ("product",)
    _translated_fields = ("head", "text")

    id = fields.IntField(pk=True)
    head = fields.CharField(max_length=256)
    head_en = fields.CharField(max_length=256, null=True)
    head_de = fields.CharField(max_length=256, null=True)
    head_fr = fields.CharField(max_length=256, null=True)
    text = fields.TextField()
    text_en = fields.TextField(null=True)
    text_de = fields.TextField(null=True)
    text_fr = fields.TextField(null=True)
    product = fields.ForeignKeyField(
        "models.Product", related_name='news', null=True
    )
    banner = fields.CharField(max_length=64, null=True)
    new_type = fields.IntField(null=True, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.head}"

    @classmethod
    async def create(
        cls: Type[MODEL], using_db: Optional[BaseDBAsyncClient] = None, **kwargs: Any
    ) -> MODEL:
        if not kwargs.get("new_type"):
            kwargs["new_type"] = None
        elif kwargs.get("new_type") \
            and kwargs.get("new_type") not in [
                str(nt.value) for nt in NewsType.__members__.values()
            ]:
            kwargs["new_type"] = None
        if not kwargs.get("product_id"):
            kwargs["product_id"] = None

        await super().create(using_db, **kwargs)


class Bid(Model, ExtendedModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(null=True, max_length=256)
    email = fields.CharField(null=True, max_length=256)
    message = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
