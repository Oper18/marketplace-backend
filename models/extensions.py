# coding: utf-8

import datetime
import uuid


class ExtendedModel:

    _exclude = ()

    async def as_dict(self):
        res = {}
        for c in self.__dict__:
            if c[0] == "_" or c in self._exclude:
                continue
            if isinstance(getattr(self, c), datetime.datetime):
                res[c] = getattr(self, c).isoformat()
            else:
                res[c] = getattr(self, c)
        return res


class AnonymousUser(ExtendedModel):
    id = None
    email = "anonymous"

    @property
    def is_anonymous(self):
        return True
