import um


def test_single():
    assert um.count("um") == 1


def test_case():
    assert um.count("Um, UM, uM") == 3


def test_punctuation():
    assert um.count("um? Um! um...") == 3


def test_substring():
    assert um.count("yummy album umbrella") == 0


def test_multiple():
    assert um.count("Um, thanks, um, that was helpful.") == 2