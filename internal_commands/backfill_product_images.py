import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import asyncio
import re

from tortoise import Tortoise

from models.models import Product
from settings import IMG_DIR, DATABASE


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "_", (name or "").lower()).strip("_")


async def backfill():
    files = {}
    for f in os.listdir(IMG_DIR):
        full = os.path.join(IMG_DIR, f)
        if not os.path.isfile(full):
            continue
        stem, ext = os.path.splitext(f)
        if ext.lower() != ".jpg":
            continue
        files[slugify(stem)] = f

    matched, unmatched = [], []
    for product in await Product.filter(img=None):
        f = files.get(slugify(product.name))
        if f:
            product.img = f
            await product.save()
            matched.append((product.name, f))
        else:
            unmatched.append(product.name)

    print(f"Matched {len(matched)} products:")
    for name, f in matched:
        print(f"  {name!r} -> {f}")
    print(f"\nUnmatched {len(unmatched)} products (set image manually via admin panel):")
    for name in unmatched:
        print(f"  {name!r}")


async def main():
    await Tortoise.init(
        db_url="postgres://{}:{}@{}:5432/{}".format(
            DATABASE["user"],
            DATABASE["password"],
            DATABASE["address"],
            DATABASE["name"],
        ),
        modules={"models": ["models.models", "aerich.models"]},
    )
    await backfill()


if __name__ == "__main__":
    asyncio.run(main())
