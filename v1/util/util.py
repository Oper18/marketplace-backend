# coding: utf-8

from typing import List

from fastapi import APIRouter, status, Response, Request, Query
from pydantic import BaseModel, EmailStr

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from response_models import Error40xResponse
from .request_models import BidRequest

from models.models import Bid

from settings import EMAIL_ADDR, MAIL_CONF


router = APIRouter(
    prefix="/v1/util",
    tags=["util"]
)


@router.post(
    "/send_bid",
    responses={
        200: {
            "model": Error40xResponse,
            "description": "bid create success",
        },
        400: {
            "model": Error40xResponse,
            "description": "something wrong",
        },
    },
    summary="Set bid",
)
async def send_bid(
    request: Request,
    response: Response,
    contacts: BidRequest,
) -> Error40xResponse:
    await Bid.create(
        name=contacts.name,
        email=contacts.email,
        message=contacts.message,
    )
    try:
        message = MessageSchema(
            subject="Bid for product",
            recipients=[EMAIL_ADDR],
            body="<h1>New bid from {}</h1><p>{}</p><p>Contact me: {}</p>".format(contacts.name, contacts.message, contacts.email),
            subtype="html",
            )

        fm = FastMail(MAIL_CONF)
        await fm.send_message(message)
    except Exception as e:
        print("MAIL SEND FAILED: ", e)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return Error40xResponse.parse_obj({"reason": "mail send failed"})
    else:
        return Error40xResponse.parse_obj({"reason": "mail sended"})
