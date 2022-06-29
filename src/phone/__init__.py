import re
import logging
import logging.config

from phone.config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)


def _phone_format(num: str) -> str:
    """Return what I need."""
    logging.debug(f"Create correct number format from {num}")
    return f"8 ({num[1:4]}) {num[4:7]}-{num[7:9]}-{num[9:11]}"


def phone(raw_number: str) -> str:
    """Return correct phone number."""
    raw_number = _numbers_from_raw_string(raw_number)
    logging.debug(f"Input value {raw_number!r}")
    match list(raw_number):
        case ['7' | '8', '9', *args] if len(args) == 9:
            number = _phone_format(num=raw_number)
        case ['9', *args] if len(args) == 9:
            raw_number = raw_number.rjust(11, '8')
            number = _phone_format(num=raw_number)
        case _:
            number = raw_number
    logging.debug(f"Return {number!r}")
    return number


def _numbers_from_raw_string(raw_number: str) -> str:
    """Return only numbers from raw request."""
    logging.debug(f"Input value {raw_number!r}")
    pattern = re.compile(r"\d+")
    numbers = pattern.findall(raw_number)
    result = "".join(numbers)
    logging.debug(f"Return {result=!r}")
    return result


if __name__ == '__main__':
    phone('slkfjlsfjsdfj2342424ljl')
