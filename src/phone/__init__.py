import re


def _phone_format(num: str) -> str:
    """Return what I need."""
    return f"8 ({num[1:4]}) {num[4:7]}-{num[7:9]}-{num[9:11]}"


def phone(raw_number: str) -> str:
    """Return correct phone number."""
    raw_number = _numbers_from_raw_string(raw_number)
    match list(raw_number):
        case ['7' | '8', '9', *args] if len(args) == 9:
            number = _phone_format(num=raw_number)
        case ['9', *args] if len(args) == 9:
            raw_number = raw_number.rjust(11, '8')
            number = _phone_format(num=raw_number)
        case _:
            number = raw_number
    return number


def _numbers_from_raw_string(raw_number: str) -> str:
    """Return only numbers from raw request."""
    pattern = re.compile(r"\d+")
    numbers = pattern.findall(raw_number)
    return "".join(numbers)
