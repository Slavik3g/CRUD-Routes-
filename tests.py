import pytest
from app import client


def test_simple():
    mylist = [1, 2, 3, 4, 5]
    assert 3 in mylist


def test_get():
    res = client.get("/tutorials")
    assert res.status_code == 200
    assert len(res.get_json()) == 4


if __name__ == "__main__":
    pytest.main()
