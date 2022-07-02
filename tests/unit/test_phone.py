import pytest

from phone import get_formatted_phone
from phone import _numbers_from_raw_string


@pytest.mark.parametrize(
        "raw_number,expected",
        [
            ("8 912 345 67 89", "8 (912) 345-67-89"),
            ("8 (912)345-6789", "8 (912) 345-67-89"),
            ("912)345-6789", "8 (912) 345-67-89"),
            ("7912345 67-89", "8 (912) 345-67-89"),
            ("+79123456789", "8 (912) 345-67-89"),
            ("+7 912-(34)-5-6-7-89", "8 (912) 345-67-89"),
            ("3 45 678 90-98-76-54-32", "3456789098765432"),
            ("(123) 456 78 91", "1234567891")
        ])
def test_phone(raw_number, expected):
    assert get_formatted_phone(raw_number) == expected


@pytest.mark.parametrize(
        "raw_string,expected",
        [
            ("+asdf123", "123"),
            ("skdfsf", ""),
            ("9-12)", "912"),
            ("123", "123"),
        ])
def test_numbers_from_raw_string(raw_string, expected):
    assert _numbers_from_raw_string(raw_string) == expected
