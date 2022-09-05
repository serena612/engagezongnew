# coding: utf-8


__all__ = (
    '_safe_string_formatter',
)


def _safe_string_formatter(user, data='', extra={}):
    _format = {
        'nickname': user.nickname or '',
        'coins': user.coins or 0,
        **extra
    }

    return data.format(**_format) if not user.is_anonymous else data
