# coding: utf-8

"""
Serve files from the local `static/` directory through the API itself
(reachable as /api/static/<path> given the app's root_path="/api"),
so `img`/`banner` fields can point at a path served by this same app
instead of relying on nginx to expose the static directory separately.
"""

import mimetypes
import os

from aiofile import async_open

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from settings import STATIC_DIR

router = APIRouter()


@router.get("/static/{file_path:path}")
async def get_static_file(file_path: str):
    full_path = os.path.normpath(os.path.join(STATIC_DIR, file_path))
    if os.path.commonpath([full_path, STATIC_DIR]) != STATIC_DIR or not os.path.isfile(full_path):
        raise HTTPException(status_code=404, detail="Not found")

    async with async_open(full_path, "rb") as f:
        content = await f.read()

    content_type, _ = mimetypes.guess_type(full_path)
    return Response(content=content, media_type=content_type or "application/octet-stream")
