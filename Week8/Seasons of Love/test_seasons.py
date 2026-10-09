from seasons import minutes_since_birth


def test_one_year():
    assert minutes_since_birth("2025-10-08") == 525600


def test_two_years():
    assert minutes_since_birth("2024-10-08") == 1052640


def test_invalid_date():
    try:
        minutes_since_birth("2025-10-32")
        assert False
    except ValueError:
        assert True