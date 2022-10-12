# coding: utf-8

import datetime
import uuid

from enum import Enum


class ExtendedModel:

    _exclude = ()
    _translated_fields = ()

    async def as_dict(self, lang="_ru"):
        res = {}
        for c in self.__dict__:
            if c[0] == "_" or c in self._exclude:
                continue
            k = c
            if lang != "_ru" and c[-3:] == lang and c[:-3] in self._translated_fields:
                k = c[:-3]
            elif lang != "_ru" and c[-3:] != lang and c[:-3] in self._translated_fields:
                continue
            elif lang == "_ru" and c[:-3] in self._translated_fields:
                continue
            elif lang != "_ru" and c in self._translated_fields:
                continue
            if isinstance(getattr(self, c), datetime.datetime):
                res[k] = getattr(self, c).isoformat()
            else:
                res[k] = getattr(self, c)
        return res


class AnonymousUser(ExtendedModel):
    id = None
    email = "anonymous"

    @property
    def is_anonymous(self):
        return True


class NewsType(Enum):
    top_drop_down = 1

