from VanityPlate import *

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True


def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS") == True


def test_first_two_letters():
    assert is_valid("50CS") == False
    assert is_valid("5CS") == False
    assert is_valid("C50") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False