# coding: utf-8

from inspect import getsourcefile

__all__ = (
    "EngageException",
)

class EngageException(Exception):
    """ Engage Exception """

    def __init__(self, fn, msg):
        self.fn = fn
        self.msg = msg

        super().__init__(self.msg)

    def __str__(self):
        return f"function name: {self.fn.__name__} -> path: {getsourcefile(self.fn)} -> errorMsg: {self.msg}"

