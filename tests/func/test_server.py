import pytest

from phone.server import app
from fastapi.testclient import TestClient


client = TestClient(app)


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
def test_api_phone(raw_number, expected):
    data = {'phone': raw_number}
    response = client.post("/unify_phone_from_json/", json=data)
    assert response.status_code == 200
    assert response.json() == expected
