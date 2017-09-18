#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import settings
from typing import Any


class DatabaseConfig(object):

    config = settings.DATABASE

    @classmethod
    def read(cls, key: str) -> Any:
        return cls.config[key]

    @classmethod
    def readline(cls, key: str) -> str:
        sentence = " ".join([k + "=" + str(v) for k, v in cls.config[key].items()])
        return sentence

    @classmethod
    def write(cls, key: str, value: str) -> None:
        cls.config[key] = value
        return None;

