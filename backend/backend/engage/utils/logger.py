# coding: utf-8

import logging; logger = logging.getLogger(__name__)

from inspect import getsourcefile

__all__ = (
    "EngageLogger",
)


class EngageLogger(Exception):
    """ Engage Logger """

    def __init__(self, fn, msg=None, isException=False): self._do_log(fn, msg, isException)

    @staticmethod
    def _do_log(fn, msg, isException):
        if isException: logger.error(f"EngageLogger >> Executing: {fn.__name__} -> path: {getsourcefile(fn)} -> errorMsg: {msg}")
        else: logger.info(f"EngageLogger >> Executing: {fn.__name__} -> path: {getsourcefile(fn)}")

