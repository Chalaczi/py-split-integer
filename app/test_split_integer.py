from app.split_integer import split_integer

def test_sum_and_length():
    result = split_integer(10, 3)
    assert sum(result) == 10
    assert len(result) == 3

def test_balanced_distribution():
    result = split_integer(10, 3)
    assert max(result) - min(result) <= 1

def test_exact_division():
    result = split_integer(9, 3)
    assert result == [3, 3, 3]

def test_remainder_distribution():
    result = split_integer(10, 3)
    assert result == [4, 3, 3]
