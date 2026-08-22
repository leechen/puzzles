import pytest

from python.recursion.serialize_json import serialize


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ({}, ""),
        ({"name": "Ada", "active": True, "score": 42}, "name:Ada;active:True;score:42"),
        (
            {"user": {"name": "Ada", "address": {"city": "London"}}},
            "user.name:Ada;user.address.city:London",
        ),
        ({"empty": {}, "answer": None}, "answer:None"),
    ],
)
def test_serialize(data, expected):
    assert serialize(data) == expected


def test_serialize_uses_parent_key_and_custom_separator():
    data = {"profile": {"name": "Ada", "roles": ["admin", "author"]}}

    assert serialize(data, parent_key="account/", sep="/") == (
        "account/profile/name:Ada;account/profile/roles:['admin', 'author']"
    )
