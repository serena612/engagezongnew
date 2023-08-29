# coding: utf-8

import threading

from functools import wraps
from django.conf import settings


# engage modules
from engage.utils import (
    EngageException as engage_exception,
    EngageLogger as engage_logger,
)

__all__ = (
    '_with',
)

# TODO: Replace Thread with celery tasks in production


class Thread(threading.Thread):
    def __init__(self, target, args=[], kwargs={}):
        super(Thread, self).__init__(target, *args, **kwargs)

    def _run(self):
        return self.run()


def _with(
    log=False,
    debug=settings.DEBUG,
    exception=settings.DEBUG,
    threading=False
):
    def wrapper(fn):
        @wraps(fn)
        def execute(*args, **kwargs):
            try:
                if log and debug: engage_logger(fn)

                # only return the data when it's a blocking function
                if threading:
                    t = Thread(target=fn(*args, **kwargs))
                    t.start()
                else:
                    return fn(*args, **kwargs)

            except Exception as why:
                if log:
                    engage_logger(fn, why, isException=True)

                if exception:
                    raise engage_exception(fn, why)

        return execute

    return wrapper
