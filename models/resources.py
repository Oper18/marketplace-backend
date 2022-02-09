# coding: utf-8

import os
import uuid
import aiofiles

from fastapi_admin.resources import Action, Field, Link, Model
from fastapi_admin.widgets import displays, filters, inputs
from fastapi_admin.file_upload import FileUpload

from models.models import Product, New, ProductSerialNumber, Category, \
    Manufacturer, Bid

from settings import IMG_DIR


def filename_generator(file):
    filename = uuid.uuid4().hex + '.' + file.filename.split('.')[-1]
    return os.path.join(filename[:2], filename[2:4], filename[4:6], filename)


class MarketPlaceAdminFileUpload(FileUpload):

    async def save_file(self, filename: str, content: bytes):
        file = os.path.join(self.uploads_dir, filename)
        os.makedirs(os.path.dirname(file), exist_ok=True)
        async with aiofiles.open(file, "wb") as f:
            await f.write(content)
        return os.path.join(self.prefix, filename)


doc_upload = MarketPlaceAdminFileUpload(
    uploads_dir=IMG_DIR,
    prefix="",
    filename_generator=filename_generator,
)


class CategoryResource(Model):
    label = "Categories"
    model = Category
    page_pre_title = "Categories"
    page_title = "Categories"
    filters = [
        filters.Search(
            name="name",
            label="Category name",
            search_mode="icontains",
            placeholder="Search for category name",
        ),
    ]
    fields = [
        "id",
        Field(
            name="name",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_fr",
            label="",
            input_=inputs.Text(),
        ),
        "created_at",
        "updated_at",
    ]


class ManufacturerResource(Model):
    label = "Manufacturers"
    model = Manufacturer
    page_pre_title = "Manufacturers"
    page_title = "Manufacturers"
    filters = [
        filters.Search(
            name="name",
            label="Manufacturer name",
            search_mode="iontains",
            placeholder="Search for category name",
        ),
    ]
    fields = [
        "id",
        Field(
            name="name",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_fr",
            label="",
            input_=inputs.Text(),
        ),
        "created_at",
        "updated_at",
    ]


class ProductResource(Model):
    label = "Products"
    model = Product
    page_pre_title = "Products"
    page_title = "Products"
    filters = [
        filters.Search(
            name="name",
            label="Product name",
            search_mode="icontains",
            placeholder="Search for product name",
        ),
        filters.Search(
            name="full_name",
            label="Product full name",
            search_mode="icontains",
            placeholder="Search for product full name",
        ),
    ]
    fields = [
        "id",
        Field(
            name="name",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="name_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="full_name",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="full_name_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="full_name_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="full_name_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="description",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="description_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="description_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="description_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="sketches",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="sketches_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="sketches_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="sketches_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="img",
            label="",
            input_=inputs.Image(upload=doc_upload, null=True),
        ),
        Field(
            name="article_number",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="volume",
            label="",
            input_=inputs.Text(),
        ),
        "category",
        "manufacturer",
        "created_at",
        "updated_at",
    ]


class ProductSerialNumberResource(Model):
    label = "Product's serial numbers"
    model = ProductSerialNumber
    page_pre_title = "Product's serial numbers"
    page_title = "Product's serial numbers"
    filters = [
        filters.Search(
            name="serial_number",
            label="Serial number",
            search_mode="contains",
            placeholder="Search for product serial number",
        ),
        filters.Search(
            name="product",
            label="Product",
            search_mode="contains",
            placeholder="Search for products",
        ),
    ]
    fields = [
        "id",
        Field(
            name="serial_number",
            label="",
            input_=inputs.Number(),
        ),
        "product",
        "created_at",
        "updated_at",
    ]


class NewResource(Model):
    label = "News"
    model = New
    page_pre_title = "News"
    page_title = "News"
    filters = [
        filters.Search(
            name="head",
            label="New's head",
            search_mode="contains",
            placeholder="Search for new head",
        ),
    ]
    fields = [
        "id",
        Field(
            name="head",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="head_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="head_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="head_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="text",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="text_en",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="text_de",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="text_fr",
            label="",
            input_=inputs.Text(),
        ),
        Field(
            name="banner",
            label="",
            input_=inputs.Image(upload=doc_upload, null=True),
        ),
        "product",
        "created_at",
        "updated_at",
    ]


class BidResource(Model):
    label = "Bids"
    model = Bid
    page_pre_title = "Bids"
    page_title = "Bids"
    filters = [
        filters.Search(
            name="contacts",
            label="Contacts",
            search_mode="icontains",
            placeholder="Search for bid contacts",
        ),
    ]
    fields = [
        "id",
        "name",
        "email",
        "message",
        "created_at",
        "updated_at",
    ]
