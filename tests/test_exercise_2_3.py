import pytest


def test_import_isprime():
    from math_utils.math_utils import isprime


@pytest.mark.parametrize("value, prime", [(1, False),
                                          (2, True),
                                          (3, True),
                                          (4, False),
                                          (47, True),
                                          (100, False)])
def test_isprime(value, prime):
    from math_utils.math_utils import isprime

    assert isprime(value) == prime, "Incorrect return value from isprime"
