from TestingMyTwttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTr"


def test_numbers_and_punctuation():
    assert shorten("hello123!") == "hll123!"