# coding: utf-8

"""
Custom admin route: bulk-import product serial numbers from a plain .txt
file (one code per line). Imported codes are inserted with product=None
and can be attached to a product later from the admin panel.
"""

from fastapi import APIRouter, Depends, File, Request, UploadFile

from fastapi_admin.depends import get_current_admin, get_resources
from fastapi_admin.responses import redirect
from fastapi_admin.template import templates

from models.models import ProductSerialNumber

router = APIRouter()

RESOURCE = "productserialnumber"


@router.get(f"/{RESOURCE}/import")
async def import_serial_numbers_view(
    request: Request,
    resources=Depends(get_resources),
    admin=Depends(get_current_admin),
):
    return templates.TemplateResponse(
        f"{RESOURCE}/import.html",
        context={
            "request": request,
            "resources": resources,
            "resource": RESOURCE,
            "resource_label": "Product's serial numbers",
            "page_title": "Import serial numbers",
            "page_pre_title": "Product's serial numbers",
        },
    )


@router.post(f"/{RESOURCE}/import")
async def import_serial_numbers(
    request: Request,
    file: UploadFile = File(...),
    admin=Depends(get_current_admin),
):
    raw = await file.read()
    text = raw.decode("utf-8-sig", errors="ignore")

    seen = set()
    codes = []
    for line in text.splitlines():
        code = line.strip()
        if code and code not in seen:
            seen.add(code)
            codes.append(code)

    if codes:
        await ProductSerialNumber.bulk_create(
            [ProductSerialNumber(serial_number=code, product=None) for code in codes],
            ignore_conflicts=True,
        )

    return redirect(request, "list_view", resource=RESOURCE)
