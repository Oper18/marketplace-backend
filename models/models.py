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
    sketches = fields.CharField(max_length=2048)
    sketches_en = fields.CharField(max_length=2048, null=True)
    sketches_de = fields.CharField(max_length=2048, null=True)
    sketches_fr = fields.CharField(max_length=2048, null=True)
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
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.head}"
