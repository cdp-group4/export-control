from typing import Any


def str_to_int_or_none(s: str) -> int | None:
    return int(s) if s is not None and s.isdecimal() else None


def to_int_or_default(value: Any, default: int) -> int:
    try:
        value = int(value)
        return value
    except Exception:
        return default
