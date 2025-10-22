import pytest
from fizzbazz import fizzbazz
def test_fizzbuzz_0_return_fizzbuzz():
    result = fizzbazz(0)
    assert result == "fizzbazz"


def test_fizzbuzz_1_return_1():
    result = fizzbazz(1)
    assert result == "1"

def test_fizzbuzz_2_return_2():
    result = fizzbazz(2)
    assert result == "2"

def test_fizzbuzz_3_return_fizz():
     result = fizzbazz(3)
     assert result == "fizz"


def test_fizzbuzz_4_return_4():
    result = fizzbazz(4)
    assert result == "4"

def test_fizzbuzz_5_return_buzz():
    result = fizzbazz(5)
    assert result == "buzz"




