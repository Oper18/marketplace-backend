# coding: utf-8

from typing import Any, Type

import datetime

from tortoise.models import Model, MODEL
from tortoise import fields

from fastapi_admin.models import AbstractAdmin

from models.extensions import ExtendedModel


class Admin(AbstractAdmin):
    pass


class Product(Model, ExtendedModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    full_name = fields.CharField(max_length=512)
    description = fields.TextField()
    sketches = fields.CharField(max_length=2048)
    img = fields.CharField(max_length=64)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class ProductSerialNumber(Model, ExtendedModel):
    _exclude = ("product",)

    id = fields.IntField(pk=True)
    serial_number = fields.IntField(unique=True)
    product = fields.ForeignKeyField(
        "models.Product", related_name='serial_numbers'
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.serial_number}"


class New(Model, ExtendedModel):
    _exclude = ("product",)

    id = fields.IntField(pk=True)
    head = fields.CharField(max_length=256)
    text = fields.TextField()
    product = fields.ForeignKeyField(
        "models.Product", related_name='news', null=True
    )
    banner = fields.CharField(max_length=64, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.head}"
